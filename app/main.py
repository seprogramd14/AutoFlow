from dotenv import load_dotenv
load_dotenv()

import uvicorn
from fastapi import FastAPI
from api.requirement import router as requirement_router

app = FastAPI()
app.include_router(requirement_router)

if __name__ == "__main__":
  uvicorn.run(app=app)