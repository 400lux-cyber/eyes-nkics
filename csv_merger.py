import os
import csv
import math
import copy
import pandas as pd

TYPE = 'SP'

exp = r"F:\EYES\CSVs(HB)\octa_4\高鹏程_OS"
name_30 = os.listdir(exp)
name_30 = [os.path.splitext(name)[0][78:-20] for name in name_30]
dir = os.path.join(exp,
                   "00478_000792283500_高鹏程_OS_2023-07-30_10-22-27_Angio 18x18 1152x1152 R2_62.705_Thickness_Choroid_ETDRS环_2024-03-13_20-58-38.csv")
dfs = pd.read_csv(dir, encoding='gbk')

column = []
for index, row in dfs.iloc[0:].iterrows():
    row = row.tolist()
    for r in row:
        row.remove('-') if '-' in row else None
    row = [x for x in row if not isinstance(x, float) or not math.isnan(x)]
    for i in range(len(row) - 1):
        if i == 0:
            column.append(row[i])
        else:
            column.append('-')

first_column = ["name"]
for n in name_30:
    column[0] = n + column[0]
    first_column.extend(column)

with open('{}.csv'.format(TYPE), 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(first_column)


# first_column = df.iloc[:, 0].transpose().tolist()
# print(first_column)

def match(names):
    n = []
    name_3 = copy.deepcopy(name_30)
    for name in names:
        for name_1 in name_3:
            if name_1 in name:
                n.append(name)
                name_3.remove(name_1)
    return n


def co(path):
    df = pd.read_csv(path, encoding='utf-8')
    co = []
    for y in range(len(df.iloc[:, 0].tolist())):
        for x in range(1, 6):
            ele = df.iloc[y][x]
            try:
                ele = float(ele)
                co.append(ele)
            except ValueError:
                pass
    return co


def move(fp, type):
    for root, dirs, files in os.walk(fp):
        for dir in dirs:
            print(dir)
            file_path = os.path.join(root, dir)
            features = match(os.listdir(file_path))
            if len(features) != 29:
                continue
            c = []
            c.insert(0, dir.encode('gbk').decode('gbk'))
            for feature in features:
                path = os.path.join(file_path, feature)
                c.extend(co(path))
            with open('{}.csv'.format(type), 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(c)
                print(dir, "written")

path = r"F:\EYES\CSVs({})\octa_{}".format(TYPE, 'processed')
move(path, TYPE)
