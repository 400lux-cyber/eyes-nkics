import os
import shutil
import re

source_dir = r'F:\EYES\DATAs\octa_9'
target_dir = r'F:\EYES\CSVs(HB)\octa_9'

for root, dirs, files in os.walk(source_dir):
    for dir in dirs:
        full_dir_path = os.path.join(root, dir)
        for r, d, f in os.walk(full_dir_path):
            if 'Quantization' in d:
                source_folder = os.path.join(r, 'Quantization','黄斑')

                match = re.search(r'_[^_]*_([^_]*)_([^_]*)_', dir)
                if match:
                    result = match.group(1) + '_' + match.group(2)
                    target_folder = os.path.join(target_dir, result)
                    try:
                        shutil.copytree(source_folder, target_folder)
                    except FileExistsError:
                        target_folder+= '_extra'
                        try:
                            shutil.copytree(source_folder, target_folder)
                        except FileExistsError:
                            target_folder += '_extra'
                    print(full_dir_path)
                    break

# import csv
# import os
# import shutil
#
#
# def csv_to_dict(file_path):
#     with open(file_path, 'r', encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         result_dict = {rows[0]: rows[1] for rows in reader}
#     return result_dict
#
#
# dict_list = csv_to_dict('../index.csv')


# def get_index(item):
#     return int(dict_list.get(item, 6))
#
#
# source_dir = r'F:\2024spr\oct_png(labeled)\6'
# target_dir = r'F:\2024spr\oct_png(labeled)'
#
# # 遍历 source_dir 下的所有文件
# for root, _, files in os.walk(source_dir):
#     for file in files:
#         full_file_path = os.path.join(root, file)
#         # 使用 get_index 函数获取索引
#         file, _ = os.path.splitext(file)
#         index = get_index(file)
#         # 构造目标文件夹路径
#         target_folder = os.path.join(target_dir, str(index))
#         # 如果目标文件夹不存在，则创建
#         if not os.path.exists(target_folder):
#             os.makedirs(target_folder)
#         # 移动文件到目标文件夹
#         if index != 6:
#             shutil.move(full_file_path, target_folder)
#             print(target_folder, file)


# import os
# import shutil
# import re
# import csv
#
# source_dir = r'F:\OCTAs'
# dst = r'F:\2024spr\qcxg_proj\qcxg(od)'
# dirs = os.listdir(source_dir)
# for dir in dirs:
#     for root, _, files in os.walk(os.path.join(source_dir, dir)):
#         for file in files:
#             if "浅层血管复合体" in file and "OD" in file:
#                 try:
#                     print(os.path.join(root, file), os.path.join(dst, file))
#                     shutil.copy(os.path.join(root, file), os.path.join(dst, file))
#                     os.rename(os.path.join(dst, file), os.path.join(dst, dir) + '.png')
#                     print(dir)
#                 except FileExistsError:
#                     pass
