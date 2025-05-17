import google.generativeai as genai
import time
import csv,os
key="AIzaSyAEmbZ-_YiNuR8gL9FVwvmsyModQ75dZuE"
genai.configure(api_key=key)
model=genai.GenerativeModel("gemini-pro")
fields = ['Message', 'Contains Drug']
mydict=[]
filename = "training.csv"
file_exists = os.path.isfile(filename)
prompt = """i am creating a dataset to train a nlp model i ll provide you a sample data with that can you generate more data in that if a message contains drug name then it is suspicious message write infront of it yes if not contain drug name write no 

in this more you need is the get me both data not only drug name data i need drug name and normal chats too and its in tabular format and this is the sample data 

Tabular format not text





Message	Contains Drug

"Are you free tonight? Can you bring some 3cst@sy with you?"	Yes

"What’s the plan for the weekend? Any fresh k@sh available?"	Yes

"How’s your day going? Need some top-notch C0C@ine for the party."	Yes

"Any good recommendations for dinner spots around here?"	No

"Got any fresh M3th available? I need it for a friend."	Yes

"आज रात मिल सकते हैं क्या? मेरे पास कुछ ताजा K@sh है।"	Yes

"कृपया बताएं कि आपके पास MDMA है क्या?"	Yes

"आपका दिन कैसा है?"	No

"Looking for some high-quality H3R01N. How much is it?"	Yes

"Can you suggest a good café nearby? Also, do you have fresh 3cst@sy?"	Yes

"Got any fresh K@sh for tonight? How much is it?"	Yes

"What’s a good place to go hiking around here?"	No

"Got any fresh C0c@ine? Need it for a special occasion."	Yes

"आपके पास ताजा MDMA है क्या?"	Yes

"क्या आप मेरे लिए एक अच्छी किताब की सिफारिश कर सकते हैं?"	No

"Need some fresh M3th. How much for a good batch?"	Yes

"How’s everything going? Any chance you have some fresh K@sh?"	Yes

"Can you recommend a good movie? Also, any fresh H3R01N?"	Yes

"What’s a good spot for brunch?"	No

"Looking for some top-grade 3cst@sy. What’s the rate?"	Yes

"Got any fresh C0C@ine? Need it urgently."	Yes

"आपके पास ताजा K@sh है क्या?"	Yes

"क्या आप मुझे एक अच्छा रेस्टोरेंट बता सकते हैं?"	No

"Looking for some fresh H3R01N. What’s the price?"	Yes

"Got any reliable M3th? Need it for a gathering."	Yes

"Can you recommend a good TV show? Also, any fresh 3cst@sy?"	Yes

"What’s a good place to get coffee around here?"	No

"Got any fresh K@sh for tonight? How much is it?"	Yes

"Looking for some top-grade C0C@ine. What’s the cost?"	Yes

"आपके पास ताजा 3cst@sy है क्या?"	Yes

"क्या आप मुझे एक अच्छा फ़िल्म सुझाव दे सकते हैं?"	No

"Need some reliable M3th. How much for a good supply?"	Yes

"How’s your weekend going? Any fresh H3R01N around?"	Yes

"Can you suggest a good spot for dinner? Also, do you have fresh C0C@ine?"	Yes

"What’s the best place for a quick bite around here?"	No

"Got any fresh K@sh available? Need it urgently."	Yes

"Looking for some high-quality 3cst@sy. Got any recommendations?"	Yes

"आपके पास ताजा M3th है क्या?"	Yes

"क्या आपके पास एक अच्छी किताब का सुझाव है?"	No

"Need some top-grade H3R01N for tonight. How much is it?"	Yes

"Can you recommend a good place for brunch? Also, any fresh K@sh?"	Yes

"Got any fresh C0C@ine? How much for a good batch?"	Yes

"What’s a good spot for a weekend getaway?"	No

"Looking for some reliable 3cst@sy. Need it for a special event."	Yes

"Got any fresh M3th for tonight? How much is it?"	Yes

"आपके पास ताजा K@sh है क्या?"	Yes

"क्या आप एक अच्छी टीवी शो की सिफारिश कर सकते हैं?"	No

"Need some fresh H3R01N. How much for a good supply?"	Yes

"Can you recommend a good café around here? Also, do you have any fresh 3cst@sy?"	Yes

"What’s the best place for a quiet dinner?"	No

"Got any fresh C0C@ine? Need it for a party."	Yes

"Looking for some high-quality M3th. Got any recommendations?"	Yes

"आपके पास ताजा 3cst@sy है क्या?"	Yes

"क्या आप एक अच्छा रेस्टोरेंट सुझा सकते हैं?"	No

"Need some reliable H3R01N. How much for a good batch?"	Yes

"How’s your day going? Any fresh K@sh available?"	Yes

"Can you suggest a good spot for lunch? Also, do you have fresh C0C@ine?"	Yes

"What’s the best place to get a coffee around here?"	No

"Got any fresh 3cst@sy for tonight? How much is it?"	Yes

"Looking for some top-grade M3th. What’s the cost?"	Yes

"आपके पास ताजा K@sh है क्या?"	Yes

"क्या आप मुझे एक अच्छा फिल्म का सुझाव दे सकते हैं?"	No

"Need some fresh H3R01N. How much for a good supply?"	Yes

"How’s everything going? Any chance you have some fresh 3cst@sy?"	Yes

"Can you recommend a good place for dinner? Also, any fresh M3th?"	Yes

"What’s a good spot for a weekend trip?"	No

"Got any fresh K@sh available? Need it urgently."	Yes

"Looking for some reliable C0C@ine. Got any recommendations?"	Yes

"आपके पास ताजा H3R01N है क्या?"	Yes

"क्या आपके पास एक अच्छी किताब का सुझाव है?"	No

"Need some fresh 3cst@sy. How much for a good supply?"	Yes

"Can you suggest a good TV show? Also, do you have any fresh K@sh?"	Yes

"Got any fresh C0C@ine for tonight? How much is it?"	Yes

"Looking for some high-quality M3th. What’s the rate?"	Yes

"What’s the best place to get coffee around here?"	No

"Got any fresh H3R01N? Need it urgently."	Yes

"Can you recommend a good movie? Also, any fresh 3cst@sy?"	Yes

"How’s your day going? Any fresh K@sh available?"	Yes

"आपके पास ताजा C0C@ine है क्या?"	Yes

"क्या आप एक अच्छा रेस्टोरेंट सुझा सकते हैं?"	No

"Looking for some reliable M3th. Need it for a party."	Yes

"Got any fresh H3R01N for tonight? How much is it?"	Yes

"What’s the best place for a quick lunch?"	No

"Need some top-grade 3cst@sy. How much for a good batch?"	Yes

"Can you recommend a good café around here? Also, do you have fresh K@sh?"	Yes

"Got any fresh C0C@ine? What’s the price?"	Yes

"Looking for some high-quality M3th. Need it urgently."	Yes

"आपके पास ताजा 3cst@sy है क्या?"	Yes

"क्या आप मुझे एक अच्छा किताब सुझाव दे सकते हैं?"	No

"Need some reliable H3R01N. How much for a good supply?"	Yes

"Can you suggest a good spot for dinner? Also, any fresh 3cst@sy?"	Yes

"What’s the best place to get a coffee?"	No

"Got any fresh K@sh available? Need it for tonight."	Yes

"Looking for some top-grade C0C@ine. What’s the rate?"	Yes

"आपके पास ताजा M3th है क्या?"	Yes

"क्या आप एक अच्छा फिल्म सुझाव दे सकते हैं?"	No

"Need some fresh 3cst@sy. How much for a good supply?"	Yes

"How’s your weekend going? Any fresh H3R01N around?"	Yes

"Can you recommend a good place for brunch? Also, do you have fresh K@sh?"	Yes

"What’s a good spot for a quick coffee?"	No

"Got any fresh C0C@ine? How much for a good batch?"	Yes

"Looking for some reliable M3th. What’s the price?"	Yes

"आपके पास ताजा 3cst@sy है क्या?"	Yes

"क्या आप एक अच्छा टीवी शो सुझाव दे सकते हैं?"	No

"Need some top-grade H3R01N. How much for a good batch?"	Yes

"Can you recommend a good café nearby? Also, any fresh K@sh?"	Yes

"Got any fresh C0C@ine? What’s the cost?"	Yes

"Looking for some reliable M3th. Need it for a special event."	Yes

"आपके पास ताजा K@sh है क्या?"	Yes

"क्या आप एक अच्छा रेस्टोरेंट सुझा सकते हैं?"	No

"Need some fresh 3cst@sy. How much for a good batch?"	Yes

"What’s the best place to go for a weekend getaway?"	No

"Got any fresh K@sh for tonight? How much is it?"	Yes

"Looking for some high-quality C0C@ine. What’s the rate?"	Yes

"आपके पास ताजा H3R01N है क्या?"	Yes

"क्या आप मुझे एक अच्छी फिल्म का सुझाव दे सकते हैं?"	No


create minimum 200 records


i don't want a code give me direct records"""
while True:
    try:
        answer = model.generate_content(prompt)
        content=answer.text
        if "|" not in content:
            continue
        content_list=content.split("\n")
        new_content=[]
        for i in content_list:
            if "|" in i and "---" not in i:  # Filter out unwanted lines like "--- ---"
                new_content.append(i)
        for i in new_content[2:]:
            line=i.split("|")
            message={}
            # print(line)
            try:
                string=str(line[1]).replace('"','')
                string=string.replace("'","")
                drug=str(line[2]).replace('"','')
                drug=drug.replace("'","")
                message["Message"]=string
                message["Contains Drug"]=drug
                # print(message)
                mydict.append(message)
            except:
                pass
        with open(filename, 'a', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            
            # Only write header if file doesn't exist yet
            if not file_exists:
                writer.writeheader()
                file_exists = True

            # Write the data rows
            writer.writerows(mydict)
        
        print("Data written successfully.")
    except Exception as e:
        print("error",e)
        print("Sleeping for 10 seconds")
        time.sleep(10)
# print(new_content)