from fastapi import FastAPI
import httpx



app = FastAPI()

@app.post("/parse_text")
def parse_text(website_url: str):
    # Здесь вы можете добавить логику парсинга текста с веб-страницы
    # В данном примере мы просто возвращаем текст в верхнем регистре
    parsed_text = website_url.upper()

    # Отправляем результат второму API
    second_api_url = "http://127.0.0.1:8001/process_text"
    with httpx.Client() as client:
        response = client.post(second_api_url, json={"parsed_text": parsed_text})

    return {"parsed_text": parsed_text, "response_from_second_api": response.json()}