import os
import pandas as pd

# 指定YOLOv5根目录
yolov5_root = "D:/huasheng/yolov5-master"

# 指定runs文件夹路径
runs_folder = os.path.join(yolov5_root, "runs")

# 指定detect文件夹路径
detect_folder = os.path.join(runs_folder, "detect")

# 获取detect文件夹下所有的exp文件夹
exp_folders = [folder for folder in os.listdir(detect_folder) if folder.startswith("exp10")]

# 根据文件夹的创建日期排序
exp_folders.sort(key=lambda x: os.path.getctime(os.path.join(detect_folder, x)))

# 获取最新创建的exp文件夹
latest_exp_folder = os.path.join(detect_folder, exp_folders[-1])

# 指定location_center文件夹路径
location_center_folder = os.path.join(latest_exp_folder, "location_center")

# 遍历location_center文件夹
for file_name in os.listdir(location_center_folder):
    if file_name.endswith(".txt"):
        file_path = os.path.join(location_center_folder, file_name)

        # 创建一个空的DataFrame来保存结果
        result_df = pd.DataFrame(columns=["File", "hao", "lan", "Sum", "Percentage", "Grade"])

        # 读取txt文件内容
        with open(file_path, "r") as file:
            lines = file.readlines()

        # 解析hao和lan的值
        hao_value = int(lines[0].strip().split(":")[1])
        lan_value = int(lines[1].strip().split(":")[1])

        # 计算相加后的结果
        sum_value = hao_value + lan_value

        # 计算百分比
        percentage = (lan_value / sum_value) * 100

        # 分级计算
        if percentage == 0:
            grade = 1
        elif 0 < percentage <= 10:
            grade = 3
        elif 10 < percentage <= 25:
            grade = 5
        elif 25 < percentage <= 50:
            grade = 7
        else:
            grade = 9

        # 将结果添加到DataFrame中
        result_df = pd.DataFrame({
            "File": [file_name],
            "hao": [hao_value],
            "lan": [lan_value],
            "Sum": [sum_value],
            "Percentage": [percentage],
            "Grade": [grade]
        })

        # 指定保存Excel文件的路径，保存到exp文件夹下
        excel_filename = f"{os.path.splitext(file_name)[0]}.xlsx"
        excel_path = os.path.join(latest_exp_folder, excel_filename)

        # 将DataFrame保存为Excel文件
        result_df.to_excel(excel_path, index=False)