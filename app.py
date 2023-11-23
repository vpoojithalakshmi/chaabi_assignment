
# from flask import Flask, request, redirect
# from flask_restful import Resource, Api
# from flask_cors import CORS
# import os
# import prediction

# app = Flask(__name__)
# cors = CORS(app, resources={r"*": {"origins": "*"}})
# api = Api(app)

# class Test(Resource):
#     def get(self):
#         return 'Welcome to, Test App API!'

#     def post(self):
#         try:
#             value = request.get_json()
#             if(value):
#                 return {'Post Values': value}, 201

#             return {"error":"Invalid format."}

#         except Exception as error:
#             return {'error': error}

# class GetPredictionOutput(Resource):
#     def get(self):
#         return {"error":"Invalid Method."}

#     def post(self):
#         try:
#             data = request.get_json()
#             predict = prediction.predict_mpg(data)
#             predictOutput = predict
#             return {'predict':predictOutput}

#         except Exception as error:
#             return {'error': error}

# api.add_resource(Test,'/')
# api.add_resource(GetPredictionOutput,'/getPredictionOutput')




# import torch
# from datasets import load_dataset
# from transformers import pipeline
# from sentence_transformers import SentenceTransformer
# from qdrant_client import QdrantClient
# from qdrant_client.http import models
# from tqdm.auto import tqdm
from typing import List
# import pandas as pd
from flask import Flask, request, jsonify
import os
import pickle

app = Flask(__name__)

# Load your question-answering model and related functions

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def get_relevant_plot(question: str, top_k: int) -> List[str]:
    try:
        encoded_query = retriever.encode(question).tolist()  # generate embeddings for the question

#         payload_filter = {
#             "column_name": "desired_value"
#         }

        result = client.search(
            collection_name=collection_name,
            query_vector=encoded_query,
            limit=top_k,
        )  # search qdrant collection for context passage with the answer
#         print(result)
        context = [
            [x.payload["product"], x.payload["description"]] for x in result
        ]  # extract title and payload from result
        return context

    except Exception as e:
        print({e})

def extract_answer(question, context):
    # Your implementation for extracting an answer
    # Replace this with your actual implementation
    pass

# API route for receiving questions and returning answers
@app.route('/qa', methods=['POST'])
def qa_endpoint():
    data = request.get_json(force=True)
    question = data['question']

    # Get relevant context
    context = get_relevant_plot(question, top_k=5)

    # Extract answer
    answer = extract_answer(question, context)

    return jsonify({'answer': answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)