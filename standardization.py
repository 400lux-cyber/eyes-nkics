import os
import pandas as pd

standard_rows = [
    "0-1mm", "0-3mm", "0-6mm", "0-9mm", "0-12mm", "0-15mm", "0-18mm",
    "1-3mm", "1-6mm", "1-9mm", "1-12mm", "1-15mm", "1-18mm",
    "3-6mm", "3-9mm", "3-12mm", "3-15mm", "3-18mm",
    "6-9mm", "6-12mm", "6-15mm", "6-18mm",
    "9-12mm", "9-15mm", "9-18mm",
    "12-15mm", "12-18mm",
    "15-18mm"
]


def process_csv(file_path, output_path):
    try:
        df = pd.read_csv(file_path, encoding='gbk')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='utf-8')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    print(f"Columns in {file_path}: {df.columns.tolist()}")

    if 'diameter(mm)' in df.columns.tolist():
        standard_df = pd.DataFrame({"diameter(mm)": standard_rows})
        merged_df = standard_df.merge(df, on="diameter(mm)", how="left")
        merged_df.to_csv(output_path, index=False)


for i in range(4, 13):
    input_directory = "F:\\EYES\\CSVs(HB)\\octa_{}".format(i)
    output_directory = "F:\\EYES\\CSVs(HB)\\octa_processed"

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                out_directory = os.path.join(output_directory, os.path.basename(root))
                os.makedirs(out_directory, exist_ok=True)
                output_path = os.path.join(out_directory, file)
                process_csv(file_path, output_path)

print("CSV文件处理完成")
