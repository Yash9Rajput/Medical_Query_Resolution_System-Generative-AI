from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Medical Query Resolution System is running."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")

    # TODO: integrate LangChain + Pinecone search here
    response = f"Dummy response for query: {query}"

    return jsonify({"query": query, "answer": response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
