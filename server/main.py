from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routers import summary

app = FastAPI(
    title="SynthUp API", version="1.0.0", description="SynthUp API documentation 🚀"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods like GET, POST, OPTIONS
    allow_headers=["*"],  # Allows all headers like Content-Type, Authorization
)


@app.get("/ping")
def ping():
    return {"message": "pong"}


app.include_router(summary.router, prefix="/api/v1", tags=["Summary"])
