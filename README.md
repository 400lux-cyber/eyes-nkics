**DATAs**路径下是若干批次原始数据

**oct_png(labeled)**是使用标签分类后的png格式眼底彩照，6类表示无标签

**OCTAs**文件夹存放了每个患眼的octa结果图

**octa(labeled)**是使用标签分类后的octa，6类表示无标签

**index.csv、E_index.csv、i.csv**是英文和中文的标签

**两个CSVs文件夹**存放了若干批次数据的黄斑（HB）和视盘（SP）的数据指标



**csv_retriever**用于检索csv文件，有些缺少行，有些有多余行

**standardization**将所有csv文件的格式统一，删除多余行，空格填充缺少行

**csv_merger1和csv_merger2**将所有批次符合要求的的csv文件复制到一个octa_processed路径下，同时去重



**oct_name_operater**将初始oct的tiff重命名之后转化为png文件

