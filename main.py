from fastapi import FastAPI
from recommender import hybrid_recommend

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Netflix Recommender API"}

@app.get("/recommend")
def recommend(user_id: int, movie_name: str):
    return {
        "recommendations": hybrid_recommend(user_id, movie_name)
    }
