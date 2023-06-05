from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file = file_path

    def list_movies(self):
      """Returns a dictionary of dictionaries that
      contains the movies information in the database.
      The function loads the information from the JSON
      file and returns the data. """
      with open(self.file, "r") as fileobj:
        movies = json.load(fileobj)
        return movies

    def add_movie(self, title, year, rating, url):
      """Adds a movie to the movies database.
      Loads the information from the JSON file, add the movie,
      and saves it. The function doesn't need to validate the input."""

      with open(self.file, "r") as fileobj:
        movies = json.load(fileobj)
      movies[title] = {"title": title, "rating": rating, "year of release": year, "image url": url}
      with open(self.file, "w") as fileobj:
        movies = json.dumps(movies)
        fileobj.write(movies)

    def delete_movie(self, title):
      """Deletes a movie from the movies database.
      Loads the information from the JSON file, deletes the movie,
      and saves it. The function doesn't need to validate the input."""
      
      with open(self.file, "r") as fileobj:
        movies = json.load(fileobj)
      del movies[title]
      with open(self.file, "w") as fileobj:
        movies = json.dumps(movies)
        fileobj.write(movies)

    def update_movie(self, title, rating):
      """Updates a movie from the movies database.
      Loads the information from the JSON file, updates the movie,
      and saves it. The function doesn't need to validate the input."""

      with open(self.file, "r") as fileobj:
        movies = json.load(fileobj)
        movies[title]["rating"] = rating
      with open(self.file, "w") as fileobj:
        movies = json.dumps(movies)
        fileobj.write(movies)