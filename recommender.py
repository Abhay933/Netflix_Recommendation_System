# Import Libraries - 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets -
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Clean genre text -
movies["genres"] = movies["genres"].str.replace("|", " ")

# Convert genres into numeric form -
cv = CountVectorizer()
genre_matrix = cv.fit_transform(movies["genres"])

# Calculate similarity between movies -
similarity = cosine_similarity(genre_matrix)


# Content-Based Recommendation -

def recommend_movie(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]

    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in scores[1:6]:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations



# User-Based Recommendation -

data = ratings.merge(movies, on="movieId")

def recommend_for_user(user_id):
    user_data = data[data["userId"] == user_id]
    liked_movies = user_data[user_data["rating"] >= 4]

    if liked_movies.empty:
        return ["Not enough ratings from user"] 

    return liked_movies["title"].head(5).tolist()



# Hybrid Recommendation -

def hybrid_recommend(user_id, movie_name):
    content_result = recommend_movie(movie_name)
    user_result = recommend_for_user(user_id)

    final_result = list(set(content_result + user_result))
    return final_result[:10]