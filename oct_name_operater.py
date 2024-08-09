# import os
#
#
# def process_string(s):
#     parts = s.split("_", 2)
#     result = "_".join(parts[:2])
#     result = result.replace("_", "").lower()
#     if "OS" in s:
#         result += "_OS.tiff"
#     if "OD" in s:
#         result += "_OD.tiff"
#     return result
#
#
# def rename_files_in_directory(directory):
#     for filename in os.listdir(directory):
#         processed_filename = process_string(filename)
#         new_filename = os.path.join(directory, processed_filename)
#         old_filename = os.path.join(directory, filename)
#         try:
#             os.rename(old_filename, new_filename)
#             print(f"Renamed {old_filename} to {new_filename}")
#         except:
#             print(f"            can't renamed {old_filename} to {new_filename}")
#
#
# rename_files_in_directory(r'F:\2024winter\proj\oct_data')


# import os
# from PIL import Image
#
#
# def convert_tiff_to_png_in_directory(directory):
#     for filename in os.listdir(directory):
#         if filename.endswith('.tiff'):
#             tiff_path = os.path.join(directory, filename)
#             png_path = os.path.join(directory, filename.replace('.tiff', '.png'))
#             img = Image.open(tiff_path)
#             img.save(png_path, 'PNG')
#             print(f"Converted {tiff_path} to {png_path}")
#
#
# # Replace 'your_directory_path' with the path of the directory you want to process
# convert_tiff_to_png_in_directory(r'F:\2024winter\proj\oct_data')


# import os
# import shutil
#
# def move_png_files(source_directory, target_directory):
#     if not os.path.exists(target_directory):
#         os.makedirs(target_directory)
#     for filename in os.listdir(source_directory):
#         if filename.endswith('.png'):
#             source_file = os.path.join(source_directory, filename)
#             target_file = os.path.join(target_directory, filename)
#             shutil.move(source_file, target_file)
#             print(f"Moved {source_file} to {target_file}")
#
# # Replace 'source_directory' and 'target_directory' with the paths of the directories you want to process
# move_png_files(r'F:\2024winter\proj\oct_data', r'F:\2024winter\proj\oct_png')


import csv
import os
import shutil


def csv_to_dict(file_path):
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        result_dict = {rows[0]: rows[1] for rows in reader}
    return result_dict


dict_list = csv_to_dict('../E_index.csv')


def get_index(item):
    return int(dict_list.get(item, 6))


def move_files_based_on_index(source_directory, target_directory_base):
    for filename in os.listdir(source_directory):
        index = get_index(filename)
        if index in [0, 1, 2, 3, 4, 5]:
            target_directory = os.path.join(target_directory_base, str(index))
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            source_file = os.path.join(source_directory, filename)
            target_file = os.path.join(target_directory, filename)
            shutil.move(source_file, target_file)
            print(f"Moved {source_file} to {target_file}")


# Replace 'source_directory' and 'target_directory_base' with the paths of the directories you want to process
move_files_based_on_index(r'F:\2024winter\proj\octa_train', r'F:\2024winter\proj\octa_sorted')
