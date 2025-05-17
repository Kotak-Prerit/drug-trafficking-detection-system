import torch
from model import BERTClassifier
from transformers import BertTokenizer
# Load the trained model
bert_model_name = "bert-base-uncased"
num_classes = 2
max_length = 128
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize tokenizer
tokenizer = BertTokenizer.from_pretrained(bert_model_name)

# Load the model
model = BERTClassifier(bert_model_name, num_classes).to(device)
model.load_state_dict(torch.load("bert_classifier.pth", map_location=device))
model.eval()

def predict_sentiment(text, max_length=96):
    model.eval()
    encoding = tokenizer(text, return_tensors='pt', max_length=max_length, padding='max_length', truncation=True)
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            _, preds = torch.max(outputs, dim=1)
    print("positive" if preds.item() == 1 else "negative")
    return "positive" if preds.item() == 1 else "negative"

# Test the model with a new input
# test_text = """
# Gelato Cake 🍰 
# my name is hardik
# """

# print(predict_sentiment(test_text, model, tokenizer, device))