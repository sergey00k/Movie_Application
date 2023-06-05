from istorage import IStorage

class StorageCsv(IStorage):
  
  def __init__(self, file_path):
    self.file = file_path

  def list_movies(self):
    """Returns a dictionary of dictionaries that
    contains the movies information in the database.
    The function loads the information from a CSV
    file and returns the data. """

    with open(self.file, "r") as fileobj:
      csv_content = fileobj.read()
      csv_list = csv_content.split("\n")
      movies = {}
      for line in csv_list[1:]:
        line_list = line.split(",")
        movies[line_list[0]] = {}
        header_list = csv_list[0].split(",")
        criteria_list = []
        for criteria in line_list:
          criteria_list.append(criteria)
        for header in header_list:
          movies[line_list[0]][header] = criteria_list[0]
          del criteria_list[0]
      return movies

  def add_movie(self, title, year, rating, url):
    """Adds a movie to the movies database.
    Loads the information from the CSV file, add the movie,
    and saves it. The function doesn't need to validate the input."""

    movies = self.list_movies()
    movies[title] = {"title": title, "rating": rating, "year of release": year, "image url": url}
    with open(self.file, "w") as fileobj:
      csv_string = "title,rating,year of release,image url"
      for key in movies:
        csv_string += "\n"
        for key, value in movies[key].items():
          csv_string += value + ","
        csv_string = csv_string[:-1]
      fileobj.write(csv_string)

  def delete_movie(self, title):
    """Deletes a movie from the movies database.
    Loads the information from the CSV file, deletes the movie,
    and saves it. The function doesn't need to validate the input."""

    movies = self.list_movies()
    del movies[title]
    with open(self.file, "w") as fileobj:
      csv_string = "title,rating,year of release,image url"
      for key in movies:
        csv_string += "\n"
        for key, value in movies[key].items():
          csv_string += value + ","
        csv_string = csv_string[:-1]
      fileobj.write(csv_string)

  def update_movie(self, title, rating):
    """Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input."""

    movies = self.list_movies()
    movies[title]["rating"] = rating
    with open(self.file, "w") as fileobj:
      csv_string = "title,rating,year of release,image url"
      for key in movies:
        csv_string += "\n"
        for key, value in movies[key].items():
          csv_string += value + ","
        csv_string = csv_string[:-1]
      fileobj.write(csv_string)

