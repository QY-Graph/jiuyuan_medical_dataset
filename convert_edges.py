import csv
import json
import os

# 定义输入和输出目录
input_directory_path = '/home/miao/knowledge_graph/medical/edges/'
output_directory_path = '/home/miao/knowledge_graph/medical/edges_jiuyuan/'

# 确保输出目录存在
if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

# 遍历输入目录下的所有CSV文件
for filename in os.listdir(input_directory_path):
    if filename.endswith('.csv'):  # 确保处理的是CSV文件
        # 定义输入文件的完整路径
        input_file_path = os.path.join(input_directory_path, filename)
        
        # 打开输入的CSV文件，并读取数据
        with open(input_file_path, mode='r', encoding='utf-8') as infile:
            # 使用csv.reader读取CSV文件
            reader = csv.reader(infile)
            
            # 跳过标题行
            next(reader)

            # 读取所有行数据
            rows = list(reader)
        
        # 解析每一行JSON数据，并提取信息
        data = []
        # 准备输出文件的表头
        headers = None

        for row in rows:
            a_id, a_labels, b_id, b_labels, relation_str = row
            json_data = json.loads(relation_str)
            properties = json_data['properties']
            a_label = a_labels.strip('[]""')  # 去除无用的字符
            b_label = b_labels.strip('[]""')
            # print(a_id, a_label, b_id, b_label)
            if headers is None:
                headers = ['start_id', 'start_vertex_type', 'end_id', 'end_vertex_type'] + list(properties.keys())  # 获取表头
            data.append([str(int(a_id) + 1), a_label, str(int(b_id) + 1), b_label] + [properties[key].replace('\n', '') for key in properties])
        
        
        # 写入输出文件
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