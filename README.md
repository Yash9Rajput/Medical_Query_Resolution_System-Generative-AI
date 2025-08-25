# Medical_Query_Resolution_System-Generative-AI

A Generative AI-powered Medical Assistant that processes PDF-based medical documents, stores embeddings in Pinecone, and answers user queries using state-of-the-art language models.

📌 Features

📄 Extracts text from PDF medical documents

✂️ Splits documents into manageable chunks

🤗 Uses Hugging Face embeddings for semantic understanding

📦 Stores embeddings in Pinecone Vector Database

🔎 Enables semantic search & query resolution

🌐 Flask-based API for interaction

🛠️ Tech Stack

Python 🐍

LangChain for orchestration

Pinecone for vector storage

Hugging Face embeddings & models

Flask for API layer

📂 Project Structure
📦 Medical_Query_Resolution_System
 ┣ 📂 src
 ┃ ┣ __init__.py
 ┃ ┣ helper.py
 ┃ ┗ prompt.py
 ┣ 📂 research
 ┃ ┗ trials.ipynb
 ┣ app.py
 ┣ store_index.py
 ┣ template.py
 ┣ requirements.txt
 ┣ setup.py
 ┣ .env (ignored)
 ┣ .gitignore
 ┣ LICENSE
 ┗ README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the root directory and add:

PINECONE_API_KEY=your_pinecone_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

▶️ Usage

Index Medical Documents

python store_index.py


Run the Flask App

python app.py

[▶️ Watch Demo](https://drive.google.com/file/d/14fCSLkmHoeGLZiL5f_aFfBgT_-p2CB7o/view?usp=sharing)