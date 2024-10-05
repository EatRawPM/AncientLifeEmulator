from os.path import join, dirname, realpath
from sys import argv
from pathlib import Path

#assets

base_path = dirname(realpath(argv[0]))

assets_path = join(base_path, 'assets')

fonts_path = join(assets_path, 'fonts')

#data

user_path = Path.home()

main_path = join(user_path, 'AppData', 'LocalLow', 'EatRawPM')