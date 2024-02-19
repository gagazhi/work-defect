import os
import shutil

# 原始文件夹路径
source_folder = 'F:/program-demo/pyqt5-demo/project1-demo/images'

# 训练集文件夹路径
train_folder = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/labels/train'

# 验证集文件夹路径
val_folder = 'F:/program-demo/pyqt5-demo/project1-demo/yolov7-main/datasets/defect/labels/val'

# 获取所有jpg文件列表
jpg_files = [f for f in os.listdir(source_folder) if f.endswith('.json')]

# 确保目标文件夹存在
if not os.path.exists(train_folder):
    os.makedirs(train_folder)

if not os.path.exists(val_folder):
    os.makedirs(val_folder)

# 按照3:7的比例分割jpg文件
train_count = int(len(jpg_files) * 0.8)
val_count = len(jpg_files) - train_count

# 将jpg文件移动到train文件夹
for i, file in enumerate(jpg_files):
    if i < train_count:
        shutil.move(os.path.join(source_folder, file), os.path.join(train_folder, file))
    else:
        shutil.move(os.path.join(source_folder, file), os.path.join(val_folder, file))

print('jpg文件已按照3:7的比例分成两份，存储在train和val文件夹中。')
