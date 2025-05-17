import os
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertModel, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# ✅ 1. Load and Preprocess Data
def load_data(data_file):
    df = pd.read_csv(data_file)
    
    # Clean Labels
    df['Contains Drug'] = df['Contains Drug'].str.strip().replace({'Yes': 1, 'No': 0})
    df.dropna(subset=['Message'], inplace=True)  # Remove missing messages
    
    # Handle Class Imbalance (Oversample "No" class)
    yes_df = df[df['Contains Drug'] == 1]
    no_df = df[df['Contains Drug'] == 0]
    no_df_upsampled = resample(no_df, replace=True, n_samples=len(yes_df), random_state=42)
    
    df_balanced = pd.concat([yes_df, no_df_upsampled]).sample(frac=1, random_state=42)
    
    texts = df_balanced['Message'].tolist()
    labels = df_balanced['Contains Drug'].tolist()
    return texts, labels


# ✅ 2. Dataset Class
class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        encoding = self.tokenizer(
            self.texts[idx], return_tensors='pt',
            max_length=self.max_length, padding='max_length', truncation=True
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(self.labels[idx])
        }

# ✅ 3. BERT Classifier Model
class BERTClassifier(nn.Module):
    def __init__(self, model_name, num_classes):
        super(BERTClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(0.1)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        x = self.dropout(outputs.pooler_output)
        return self.fc(x)

# ✅ 4. Training & Evaluation Functions
def train(model, data_loader, optimizer, scheduler, device, loss_fn):
    model.train()
    total_loss = 0

    for batch in data_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        loss = loss_fn(outputs, labels)

        loss.backward()
        optimizer.step()
        scheduler.step()
        total_loss += loss.item()

    return total_loss / len(data_loader)

def evaluate(model, data_loader, device):
    model.eval()
    predictions, actual_labels = [], []

    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            _, preds = torch.max(outputs, dim=1)

            predictions.extend(preds.cpu().tolist())
            actual_labels.extend(labels.cpu().tolist())

    return accuracy_score(actual_labels, predictions), classification_report(actual_labels, predictions)

# ✅ 5. Prediction Function
def predict_sentiment(text, model, tokenizer, device, max_length=96):
    model.eval()
    encoding = tokenizer(text, return_tensors='pt', max_length=max_length, padding='max_length', truncation=True)
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        _, preds = torch.max(outputs, dim=1)

    return "positive" if preds.item() == 1 else "negative"

# ✅ 6. Training Pipeline
if __name__ == "__main__":
    data_file = "processed_data_50k.csv"
    texts, labels = load_data(data_file)
    bert_model_name = 'bert-base-uncased'
    num_classes = 2
    max_length = 96  # Reduced from 128
    batch_size = 32  # Increased from 16
    num_epochs = 6  # Increased from 4
    learning_rate = 3e-5  # Increased slightly

    train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

    tokenizer = BertTokenizer.from_pretrained(bert_model_name)
    train_dataset = TextDataset(train_texts, train_labels, tokenizer, max_length)
    val_dataset = TextDataset(val_texts, val_labels, tokenizer, max_length)

    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=batch_size)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = BERTClassifier(bert_model_name, num_classes).to(device)

    optimizer = AdamW(model.parameters(), lr=learning_rate)
    total_steps = len(train_dataloader) * num_epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    # Apply class weights for imbalance handling
    class_weights = torch.tensor([1.0, 1.5]).to(device)
    loss_fn = nn.CrossEntropyLoss(weight=class_weights)

    # Train Model
    for epoch in range(num_epochs):
        print(f"Epoch {epoch + 1}/{num_epochs}")
        train_loss = train(model, train_dataloader, optimizer, scheduler, device, loss_fn)
        accuracy, report = evaluate(model, val_dataloader, device)

        print(f"Training Loss: {train_loss:.4f}")
        print(f"Validation Accuracy: {accuracy:.4f}")
        print(report)

    # Save Model
    torch.save(model.state_dict(), "bert_classifier.pth")

    # Test Prediction
    test_text = "How’s your day going? Need some top-notch C0C@ine for the party."
    sentiment = predict_sentiment(test_text, model, tokenizer, device)
    print(f"Predicted sentiment: {sentiment}")
