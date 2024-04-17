from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post('/process_voice')
async def process_voice(file_id: str):
    try:
        # Здесь вы можете выполнить обработку голосового сообщения, сохранение, оценку и т.д.
        # Просто для примера, возвращаем обратно тот же file_id
        return {'result': f'Successfully processed voice message with file_id: {file_id}'}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error processing voice message: {str(e)}')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=5000)
