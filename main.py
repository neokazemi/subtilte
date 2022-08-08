from filer_helper import *
from web_helper import *


def print_menu():
    print('1 -- Download Subtitle for All Files')
    print('2 -- Download Subtitle for a Specific Movie')
    print('3 -- Download Subtitle for a Specific Series')
    print('')


if __name__ == "__main__":
    print_menu()
    option = int(input('Enter Your Choice: '))
    if option == 1:  # get all
        movies = get_movies()
        download_all_movies_subtitle(movies)
