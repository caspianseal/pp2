# Function to check if the IMDB score of a movie is above 5.5
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

# Function to filter movies with an IMDB score above 5.5
def filter_above_5_5(movies):
    return [movie for movie in movies if is_above_5_5(movie)]

# Function to filter movies by category
def filter_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# Function to calculate the average IMDB score of a list of movies
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

# Function to calculate the average IMDB score of movies in a category
def average_imdb_score_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb_score(category_movies)
