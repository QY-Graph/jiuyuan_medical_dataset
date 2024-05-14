import csv
import json
import os

# 定义输入和输出目录
input_directory_path = '/home/miao/knowledge_graph/medical/vertices/'
output_directory_path = '/home/miao/knowledge_graph/medical/vertices_jiuyuan/'

# 确保输出目录存在
if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

# 遍历输入目录下的所有文件
for filename in os.listdir(input_directory_path):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        # 定义输入文件的完整路径
        input_file_path = os.path.join(input_directory_path, filename)
        
        # 打开输入的CSV文件，并读取数据
        with open(input_file_path, mode='r', encoding='utf-8') as infile:
            # 使用csv.reader读取CSV文件
            reader = csv.reader(infile)
            # 跳过可能存在的标题行
            next(reader)
            
            # 读取所有行数据
            rows = list(reader)
        
        # 解析每一行JSON数据，并提取信息
        data = []
        headers = None
        for row in rows:
            json_data = json.loads(row[0])  # 将字符串转换为JSON对象
            id = json_data['id']
            properties = json_data['properties']
            # 将id和properties中的每个key-value对添加到列表中
            if headers is None:
                headers = ['id'] + list(properties.keys())  # 获取表头
            # 点id需要从1开始
            data.append([id + 1] + [properties[key].replace('\n', '') for key in properties])
        
        # 定义输出文件的完整路径
        output_file_path = os.path.join(output_directory_path, filename)
        
        # 写入输出CSV文件，指定逗号为分隔符
        with open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')  # 指定逗号为分隔符
            # 写入表头
            writer.writerow(headers)
            # 写入数据
            writer.writerows(data)
        
        print(f'文件 {filename} 转换完成。')

print('所有文件转换完成。')
