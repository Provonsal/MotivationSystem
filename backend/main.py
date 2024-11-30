import asyncio
import uvicorn
from API.routes import app
from sql.main import init_models

if __name__ == "__main__":
    asyncio.run(init_models())
    uvicorn.run(app=app, host="0.0.0.0")