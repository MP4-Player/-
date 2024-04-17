from fastapi import FastAPI
from fastapi import Request, FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/process_text")
def process_text(parsed_text: str):
    # Здесь вы можете добавить логику обработки текста, например, нахождение часто встречающегося слова и самого длинного слова
    words = parsed_text.split()
    most_common_word = max(set(words), key=words.count)
    longest_word = max(words, key=len)
    
    return {"most_common_word": most_common_word, "longest_word": longest_word}