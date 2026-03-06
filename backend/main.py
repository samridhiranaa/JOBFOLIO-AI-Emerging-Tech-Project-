from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Jobfolio AI Backend Running"}