# 📂 Пример выполнения файловой команды (executor/file_executor.py):

import os

def rename_files(folder: str, ext: str):
    files = [f for f in os.listdir(folder) if f.endswith(f".{ext}")]
    for i, filename in enumerate(files):
        new_name = f"file_{i+1}.{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))