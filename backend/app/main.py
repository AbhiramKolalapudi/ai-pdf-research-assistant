from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Welcome to the AI PDF Research Assistant!",
        "status": "running",
        "version": "0.1.0"
    }