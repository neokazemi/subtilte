import os
import pathlib
import fnmatch


class Movie:
    def __init__(self, folder_string):
        self.name = folder_string.split("(")[0].split("-")[0].strip()
        self.year = folder_string[folder_string.find("(")+1:folder_string.find(")")]
        if len(folder_string.split('-')) > 1:
            self.name_detail = folder_string.split("-")[1].split('(')[0].strip()
        else:
            self.name_detail = ""
        self.folder_string = folder_string
        current_path = os.getcwd()
        parent_path = os.sep.join(current_path.split(os.sep)[:-1])
        movies_path = os.path.join(parent_path, "Movies")
        self.current_movie_path = os.path.join(movies_path, folder_string)
        self.file_name = self.get_file_name(movies_path)
        self.have_subtitle = bool(find_file(self.file_name + '.srt', self.current_movie_path))
        self.quality = self.get_file_quality()
        self.is_extended = 'extended' in self.file_name.lower()

    def get_file_name(self, movies_path):
        files_in_folder = os.listdir(os.path.join(movies_path, self.folder_string))
        for file in files_in_folder:
            if '.mkv' in file:
                return file.split('.mkv')[0]
            elif '.mp4' in file:
                return file.split('.mp4')[0]
        return ""

    def get_file_quality(self):
        file_name = self.file_name.lower().replace('.', '')
        if 'brrip' in file_name:
            return 'bluray'
        if 'bluray' in file_name:
            return 'bluray'
        if 'web-dl' in file_name:
            return 'webdl'
        if 'webdl' in file_name:
            return 'webdl'
        if 'webrip' in file_name:
            return 'webdl'
        if 'webrp' in file_name:
            return 'webdl'
        if 'blury' in file_name:
            return 'bluray'
        return 'bluray'

    def __repr__(self):
        return self.name + ' - ' + self.name_detail + ' - ' + self.year + ' - ' + str(self.have_subtitle) + ' - ' + self.quality


def find_file(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name.lower(), pattern):
                result.append(os.path.join(root, name))
    return result


def get_movies(debug):
    current_path = os.getcwd()
    parent_path = os.sep.join(current_path.split(os.sep)[:-1])
    movies_path = os.path.join(parent_path, "Movies")
    movies = []
    for movie_folder in os.listdir(movies_path):
        movies.append(Movie(movie_folder))
        if debug:
            print('found on disk: ', Movie(movie_folder))
    return movies
