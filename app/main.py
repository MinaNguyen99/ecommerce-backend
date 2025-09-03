from fastapi import FastAPI

app = FastAPI(title="E-commerce Backend")

@app.get("/")
def root():
    return {"message": "Hello, FastAPI E-commerce!"}
