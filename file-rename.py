import os

# Consts
path_to_books = "/Users/Evgenij 1/WEB/gdz/source/books/by-id-22-03-2021";

# Need to set
book_id = "77"
from_ = 2
to_ = 140
shift_num = 2
direction = "forward" # "forward" OR "back"


path_to_book = path_to_books + '/' + book_id + '/'

if direction == "forward":
    for i in reversed(range(from_, to_ + 1)):
        original_num = str(i).zfill(6)
        original_file_path = path_to_book + book_id + '_' + original_num + '.jpg'

        new_num = str(i + shift_num).zfill(6)
        new_file_path = path_to_book + book_id + '_' + new_num + '.jpg'

        os.rename(original_file_path, new_file_path)
else if direction == "back":
    for i in range(from_, to_ + 1):
        original_num = str(i).zfill(6)
        original_file_path = path_to_book + book_id + '_' + original_num + '.jpg'

        new_num = str(i - shift_num).zfill(6)
        new_file_path = path_to_book + book_id + '_' + new_num + '.jpg'

        os.rename(original_file_path, new_file_path)