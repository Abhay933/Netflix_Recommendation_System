from recommender import hybrid_recommend

print("🎬 Netflix-Style Movie Recommendation System\n")

user_id = int(input("Enter User ID (example: 1): "))
movie_name = input("Enter a movie you like (exact name): ")

recommendations = hybrid_recommend(user_id, movie_name)

print("\nRecommended Movies for You:")
for movie in recommendations:
    print("👉", movie)