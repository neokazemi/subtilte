import requests
from filer_helper import *
from bs4 import BeautifulSoup


class MovieResult:
    def __init__(self, folder_string):
        self.name = folder_string.split("(")[0].split("-")[0].strip()
        self.year = folder_string[folder_string.find("(")+1:folder_string.find(")")]
        if len(folder_string.split(':')) > 1:
            self.name_detail = folder_string.split(":")[1].split('(')[0].strip()
        else:
            self.name_detail = ""

    def __repr__(self):
        return self.name + ' - ' + self.name_detail + ' - ' + self.year

def get_search_results_for_movie(movie):
    movie_name_query = movie.name.replace(' ', '+')
    res = requests.get('https://subf2m.co/subtitles/searchbytitle?query=' + movie_name_query)
    soup = BeautifulSoup(res.content)
    results = []
    return res.content


def download_movie_subtitle(movie):
    print(get_search_results_for_movie(movie))


def download_all_movies_subtitle(movies):
    for movie in movies:
        download_movie_subtitle(movie)