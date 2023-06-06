def main():
    from movie_app import MovieApp
    from storage_csv import StorageCsv

    storage = StorageCsv('movies.csv')
    movie_app = MovieApp(storage)
    movie_app.main_menu()

if __name__ == "__main__":
    main()