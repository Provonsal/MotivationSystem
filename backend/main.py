import asyncio
import uvicorn
from API.routes import app

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0",)