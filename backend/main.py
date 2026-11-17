from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  dotenv import load_dotenv
import os 


app = FastAPI()
load_dotenv()

origins = [
    origin.strip()
    for origin in os.getenv("origins", "").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# defining api endpoint 
@app.get("/")
def first_example():
    return {"message": "Working"}

@app.get("/health_check")
def health():
    return {"message": "Working properly"}

@app.get("/api/feedback")
def generate_feedback():
    return {"message": "Placeholder_feedback"}

@app.get("/api/name")
def greet(name: str = "User"):
    return {"message":f"Welcome {name}"}