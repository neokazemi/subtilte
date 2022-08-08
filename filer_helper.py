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

    def get_file_name(self, movies_path):
        files_in_folder = os.listdir(os.path.join(movies_path, self.folder_string))
        for file in files_in_folder:
            if '.mkv' in file:
                return file.split('.mkv')[0]
            elif '.mp4' in file:
                return file.split('.mp4')[0]
        return ""

    def __repr__(self):
        return self.name + ' - ' + self.name_detail + ' - ' + self.year + ' - ' + str(self.have_subtitle)


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
    print(movies)
    return movies
