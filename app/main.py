from fastapi import FastAPI

app = FastAPI(title="YOLO StrongSORT API (skeleton)")

@app.get("/health")
def health():
    return {"status": "ok"}