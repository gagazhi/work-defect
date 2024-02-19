# import os
#
# # 图片文件夹路径
# image_folder = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/images/train'
#
# # 指定保存路径的文本文件名
# output_file = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/train.txt'
#
# # 获取图片文件的扩展名列表，例如 ['jpg', 'jpeg', 'png', 'gif']
# image_extensions = ['.jpg']
#
# # 打开输出文件，准备写入
# with open(output_file, 'w') as file:
#     # 遍历文件夹
#     for root, _, files in os.walk(image_folder):
#         for file in files:
#             # 如果文件扩展名在图片扩展名列表中，则认为是图片文件
#             if any(file.lower().endswith(ext) for ext in image_extensions):
#                 # 获取图片文件的完整路径
#                 image_path = os.path.join(root, file)
#                 # 将图片文件的路径写入到输出文件中
#                 file.write(image_path + '\n')
# print(f'图片文件路径已保存到 {output_file}。')

import os

# 指定包含图片的文件夹路径
image_folder_path = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/images/val'

# 指定图片的格式，例如：'*.jpg', '*.png', '*.jpeg' 等
image_format = '*.jpg'  # 修改为你的图片格式

# 指定要保存图片路径的文件
output_file_path = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/val.txt'

# 获取文件夹中的所有文件名
file_names = os.listdir(image_folder_path)

# 过滤出符合条件的图片文件名
image_names = [name for name in file_names if name.lower().endswith(image_format.lower().strip('*'))]

# 对图片文件名进行排序，确保按照名称的数字顺序排序
# 这里我们使用一个自定义的key函数，它会提取文件名中的数字部分，并将其转换为整数进行排序
image_names.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# 获取所有图片的完整路径
image_paths = [os.path.join(image_folder_path, name) for name in image_names]

# 将图片路径写入到文件中
with open(output_file_path, 'w') as file:
    for path in image_paths:
        file.write(path + '\n')

print(f'图片路径已保存到 {output_file_path} 文件中。')


