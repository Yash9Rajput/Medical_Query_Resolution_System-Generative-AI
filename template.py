import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

def get_icon(filepath: Path) -> str:
    if filepath.is_dir():
        return "📁"
    ext = filepath.suffix.lower()
    if ext == ".py":
        return "🐍"      # Python file
    elif ext == ".ipynb":
        return "📓"      # Jupyter Notebook
    elif ext == ".env":
        return "🔐"      # Env file (security)
    elif ext == ".txt":
        return "📝"      # Text file
    elif ext == ".json":
        return "🗂️"      # JSON file
    else:
        return "📄"      # Generic file icon


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    icon = get_icon(filepath)
    
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file:{filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    
    else:
        logging.info(f"{filename} is already exists")    