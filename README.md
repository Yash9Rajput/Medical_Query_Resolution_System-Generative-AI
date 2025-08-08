# Medical_Query_Resolution_System

Project Overview
This project uses the llama-cpp-python library to load and run inference on the Mistral-7B-Instruct GGUF model from TheBloke repository.


> Prerequisites

. Python 3.8 or higher

. Git Bash or a Bash-compatible terminal (Windows)

. Sufficient disk space (~4-6 GB) on the drive for the model file

. Access to the Hugging Face Hub

# Step 1: Set up Python Virtual Environment

**Create and activate a virtual environment named 'medibot'**

python -m venv medibot

source medibot/Scripts/activate

# Step 2: Install Required Python Packages

```python
sentence-transformers==2.2.2
langchain
flask
pypdf
python-dotenv
pinecone[grpc]
langchain-pinecone
langchain-community
langchain-huggingface
transformers
accelerate
huggingface_hub
llama-cpp-python
-e .

```
**Install llama-cpp-python for GGUF model support**

pip install llama-cpp-python

# Step 3: Download Mistral-7B-Instruct GGUF Model 

pip install huggingface_hub --upgrade

huggingface-cli login

Then, create the model directory and download the GGUF model file:

mkdir -p /d/models/mistral

huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir /d/models/mistral --local-dir-use-symlinks False

# Step 4: Verify Model File

Check that the model file exists on your D: drive:

ls /d/models/mistral

# Step 5: Running Inference with llama-cpp-python

from llama_cpp import Llama

model_path = "D:/models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

llm = Llama(model_path=model_path)

prompt = "Write a poem about AI."

response = llm(prompt)

print(response)

Run the script:

python run_mistral.py