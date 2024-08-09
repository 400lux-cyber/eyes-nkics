import os
import csv
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def get_csv_row_counts_and_folders(directory):
    row_count_16_folders = []
    row_count_37_folders = []

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
            if csv_files:
                first_csv_file = os.path.join(dir_path, csv_files[0])

                encoding = detect_encoding(first_csv_file)
                try:
                    with open(first_csv_file, newline='', encoding=encoding) as csvfile:
                        csvreader = csv.reader(csvfile)
                        row_count = sum(1 for row in csvreader)
                        if row_count == 16:
                            row_count_16_folders.append(dir)
                        elif row_count == 37:
                            row_count_37_folders.append(dir)
                except UnicodeDecodeError as e:
                    print(f"Error reading {first_csv_file} with encoding {encoding}: {e}")

    return row_count_16_folders, row_count_37_folders


r16, r37 = [], []

for i in range(4, 13):
    root_directory = f'F:\\EYES\\CSVs(HB)\\octa_{i}'
    row_count_16_folders, row_count_37_folders = get_csv_row_counts_and_folders(root_directory)
    r16.extend(row_count_16_folders)
    r37.extend(row_count_37_folders)

print("Folders with 16 rows CSV files:", r16)
print("Folders with 37 rows CSV files:", r37)

# import os


# def count_files_in_folders(directory):
#     folder_file_counts = set()
#
#     for root, dirs, files in os.walk(directory):
#         for dir in dirs:
#             dir_path = os.path.join(root, dir)
#             file_count = len([f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))])
#             folder_file_counts.add(file_count)
#             if file_count <30:
#                 print(dir_path)
#
#     return folder_file_counts
#
#
# # 输入目录路径
# directory = "F:\\EYES\\CSVs(SP)\\octa_processed"
#
# # 调用函数并输出结果
# folder_file_counts = count_files_in_folders(directory)
# print(folder_file_counts)
