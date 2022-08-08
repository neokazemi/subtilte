import requests
from filer_helper import *
from bs4 import BeautifulSoup


class MovieResult:
    def __init__(self, title, link):
        self.name = title.split("(")[0].split(":")[0].strip()
        self.year = title[title.find("(")+1:title.find(")")]
        if len(title.split(':')) > 1:
            self.name_detail = title.split(":")[1].split('(')[0].strip()
        else:
            self.name_detail = ""
        self.link = link

    def __repr__(self):
        return self.name + ' - ' + self.name_detail + ' - ' + self.year


def get_search_results_for_movie(movie):
    movie_name_query = movie.name.replace(' ', '+')
    res = requests.get('https://subf2m.co/subtitles/searchbytitle?query=' + movie_name_query)
    soup = BeautifulSoup(res.content, features="html.parser")
    results = []
    for link in soup.select('div.title a'):
        results.append(MovieResult(link.text, link.get('href')))
    return results


def choose_movie_result(results, movie):
    for result in results:
        if result.name.lower() == movie.name.lower():
            if result.year == movie.year:
                if result.name_detail.lower() == movie.name_detail.lower():
                    return 'https://subf2m.co' + result.link


def download_movie_subtitle(movie):
    query_results = get_search_results_for_movie(movie)
    chosen_subtitle_link = choose_movie_result(query_results, movie)
    # print(chosen_subtitle_link)


def download_all_movies_subtitle(movies, debug):
    for movie in movies:
        download_movie_subtitle(movie)