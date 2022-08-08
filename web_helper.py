import requests
from file_helper import *
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


class SubtitleResult:
    def __init__(self, html):
        self.quality = self.get_quality(html.text)
        self.rate_good = self.get_rating(html)
        self.link = self.get_link(html)

    def get_rating(self, html):
        return bool(html.select('.rate.good'))

    def get_quality(self, html):
        quality_info = html.lower().replace('.', '')
        if 'brrip' in quality_info:
            return 'bluray'
        if 'bluray' in quality_info:
            return 'bluray'
        if 'web-dl' in quality_info:
            return 'webdl'
        if 'webdl' in quality_info:
            return 'webdl'
        if 'webrip' in quality_info:
            return 'webdl'
        if 'webrp' in quality_info:
            return 'webdl'
        if 'blury' in quality_info:
            return 'bluray'
        return 'bluray'

    def get_link(self, html):
        return html.select('a.download')[0].get('href')


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


def get_subtitle_list(page_link):
    res = requests.get(page_link + '/farsi_persian/')
    soup = BeautifulSoup(res.content, features="html.parser")
    results = []
    for link in soup.select('li.item'):
        results.append(SubtitleResult(link))
    return results


def download_movie_subtitle(movie):
    query_results = get_search_results_for_movie(movie)
    chosen_movie_link = choose_movie_result(query_results, movie)
    available_subtitle_list = get_subtitle_list(chosen_movie_link)


def download_all_movies_subtitle(movies, debug):
    for movie in movies:
        download_movie_subtitle(movie)