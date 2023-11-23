# Chaabi_assignment

## Overview of the model:
- Used Qdrant Vector base to store the embeddings of given data
- Concatenated product name, category, sub category, brand and description data of each product into vectors
- Implemented BERT LLM model on the top matched products obtained from similarity search from vector base to get output
- Wrapped the model as an REST API using Flask 

## Instructions to run the API:
- Clone the repository and go into that directory
- Run "python app.py"
- Access the API by address http://127.0.0.1:5000/
- Use an application called Postman to test the API. Link for the app: https://www.postman.com/downloads/
- Create an account and get started in the app
- Select POST and paste the URL there
- Go into the Body and select raw. Open JSON file as input and type your query
- Click on SEND to send the request to the model and get the output below
  

## Sample Queries:

question = "which product is produced by Nutrashil brand"
  Answer:  Nutriorg Jamun Honey 
  Title:  Certified Organic Jamun Honey 
  score:  0.7772384881973267

question = "Which product contains garlic oil"
  Answer:  Colavita Extra Virgin Olive Oil 
  Title:  Garlicolio - Garlic Seasoning Made With Extra Virgin Olive Oil 
  score:  0.5382457971572876

question = "What is called as Indian superfruit and also an Indian gooseberry?"
  Answer:  amla 
  Title:  Amla 
  score:  0.9943625330924988

question = "What wax is a sculpting product in the Schwarzkopf line? "
  Answer:  Taft Hair Wax 
  Title:  Taft Shine Gel Wax 
  score:  0.8936730027198792

question = "What is the size of designer glass bowl? "
  Answer:  280 ML 
  Title:  Designer Glass Bowl 
  score:  0.7578027248382568

