import requests
import json

class MovieApp:
  def __init__(self, storage):
    print("\n********** My Movies Database **********\n")
    self.storage = storage
    self.movies = storage.list_movies()
    

  def main_menu(self):
    """ opens the main menu where user selects options"""
    
    self.movies = self.storage.list_movies()
    print("\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n9. Generate website")
    selection = input("\nEnter choice (1-9): ")
    if selection == "0":
      return print("Bye!")
    if selection == "1":
      self._list_movies()
    if selection == "2":
      self._add_movie()
    if selection == "3":
      self._delete_movie()
    if selection == "4":
      self._update_movie()
    if selection == "5":
      self._stats()
    if selection == "6":
      self._random_movie()
    if selection == "7":
      self._search_movie()
    if selection == "8":
      self._sort_by_rating()
    if selection == "9":
      self._generate_website()

  def _list_movies(self):
    """lists movies in the database"""

    self.total = len(self.movies)
    print(f"\n{self.total} movies in total")
    for movie in self.movies:
      print(f"{self.movies[movie]['title']}: {self.movies[movie]['rating']}, {self.movies[movie]['year of release']}")
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _add_movie(self):
    """adds movie to database using api fetching"""

    self.title = input('\nEnter a movie name: ')
    payload = {'apikey': '3d01cfe1', 't': self.title}
    response = requests.get('http://www.omdbapi.com/', params=payload)
    if response.status_code != 200:
      print("Error retrieving data from api.")
    else:
      content = response.json()
      if 'Error' in content:
        print(content['Error'])
      else:
        self.storage.add_movie(self.title, content['Year'], content['imdbRating'], content['Poster'])
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _delete_movie(self):
    """deletes movie from database manually"""

    movie = input('\nEnter movie name to delete: ')
    self.storage.delete_movie(movie)
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _update_movie(self):
    """updates movie in database manually"""

    movie = input('\nEnter a movie name: ')
    if movie not in self.movies:
      print("\nError movie is not in database.")
    else:
      rating = input('\nEnter movies rating: ')
    self.storage.update_movie(movie, rating)
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _stats(self):
    """shows stats of movies in the database"""

    sum = 0
    rating_list = []
    for movie in self.movies:
      rating = self.movies[movie]['rating']
      sum += float(rating)
      rating_list.append(rating)
    rating_list.sort(reverse=True)
    print(f"\nAverage rating: {sum / len(rating_list)}")
    median_calc = int(len(rating_list) / 2)
    if len(rating_list) % 2 == 0:
      print(f"Median rating: {(float(rating_list[median_calc - 1]) + float(rating_list[median_calc])) / 2}")
    else:
      print(f"Median rating: {rating_list[median_calc]}")
    for movie in self.movies:
      if rating_list[0] == self.movies[movie]['rating']:
        print(f"Best movie: {self.movies[movie]['title']}, {rating_list[0]}")
      if rating_list[-1] == self.movies[movie]['rating']:
        print(f"Worst movie: {self.movies[movie]['title']}, {rating_list[-1]}")
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _random_movie(self):
    """shows a random movie from the database"""

    import random
    random_movie = random.choice(list(self.movies))
    print(f"\nRandom movie with its rating: {random_movie}, {self.movies[random_movie]['rating']}")
    input("\nPress enter to continue\n")
    self.main_menu()

  def _search_movie(self):
    """searches for a specific movie in the database"""

    search = input("\nEnter part of movie name: ")
    search_results = 0
    for movie,rating in self.movies.items():
      if search.lower() == movie.lower()[:len(search)]:
        print(f"{movie}: {self.movies[movie]['rating']}, {self.movies[movie]['year of release']}")
        search_results += 1
    if search_results == 0:
      print("No movies match your search criteria.")
    input("\nPress enter to continue\n")
    self.main_menu()
  
  def _sort_by_rating(self):
    """lists movies in database sorted by rating"""

    print("\n")
    copy = self.movies.copy()
    top_movie = 0
    top_rating = 0
    movies_descending = []
    ratings_descending = []
    for movie in range(len(self.movies) + 1):
      if top_movie != 0:
        movies_descending.append(top_movie)
        ratings_descending.append(top_rating)
        top_rating = 0
        del copy[top_movie]
      for movie in copy:
        if float(copy[movie]['rating']) > float(top_rating):
          top_rating = self.movies[movie]['rating']
          top_movie = movie
    for index,movie in enumerate(movies_descending):
      print(f"{movie}, {ratings_descending[index]}")
    input("\nPress enter to continue\n")
    self.main_menu()

  def _generate_website(self):
    """Generates website using html"""

    with open("_static/index_template.html", "r") as html_file:
      pure_html = html_file.read()
      template_start = 0
      template_end = 0
      for index, letter in enumerate(pure_html):
        if template_start == 0:
          if letter == "<":
            if pure_html[index + 1] == "l":
              if pure_html[index + 2] == "i":
                if pure_html[index + 3] == ">":
                  template_start = index
        elif letter == "<":
          if pure_html[index + 1] == "/":
            if pure_html[index + 2] == "o":
              if pure_html[index + 3] == "l":
                if pure_html[index + 4] == ">":
                  template_end = index + 4
                  break
      html_template = pure_html[template_start:template_end]
      html_movie_insertion = []
      for index, letter in enumerate(html_template):
        if letter == "<":
          if html_template[index + 1] == "/":
            if html_template[index + 2] == "l":
              if html_template[index + 3] == "i":
                if html_template[index + 4] == ">":
                  needed_template_end = index + 5
                  break
      html_template = html_template[:needed_template_end]
      list_of_template = html_template.split("\n")
      template_copy = html_template
      for movie in self.movies:
        html_template = html_template.replace(list_of_template[2], f'''<img class="movie-poster" src="{self.movies[movie]['image url']}">''')
        html_template = html_template.replace(list_of_template[3], f'''<div class="movie-title">{self.movies[movie]['title']}</div>''')
        html_template = html_template.replace(list_of_template[4], f'''<div class="movie-year">{self.movies[movie]['year of release']}</div>''')
        html_movie_insertion.append(html_template)
        html_template = template_copy
      html_movie_insertion = ' '.join(html_movie_insertion)
      pure_html = pure_html.replace(pure_html[template_start:template_end - 4], html_movie_insertion)
      with open("_static/index_template.html", "w") as html_file:
        html_file.write(pure_html)
    self.main_menu()
