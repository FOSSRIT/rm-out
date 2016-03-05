import os


class Board:
    def get_directories():
        return [f for f in os.listdir('.') if not os.path.isfile(f)]

    def get_files():
        return [f for f in os.listdir('.') if os.path.isfile(f)]

