from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.requirement import router as requirement_router
from api.page import router as page_router

app = FastAPI()
app.include_router(requirement_router)
app.include_router(page_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)