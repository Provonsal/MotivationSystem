from API.app import app


# такой шаблон рутов
@app.get("/")
async def root():
    return {"message": "Hello World"}