#Write your lambda function here
rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"


print(rate_movie(9.2))
print(rate_movie(7.2))
