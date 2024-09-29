import os


def remove_empty_folders(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder in dirs[:]:  # 使用dirs[:]来避免在迭代时修改dirs列表
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


directory_path = r"D:\test"

remove_empty_folders(directory_path)
