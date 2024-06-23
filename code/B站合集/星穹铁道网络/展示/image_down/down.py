import pandas as pd
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 读取CSV文件
df = pd.read_csv('nodes.csv')

# 创建存储头像的目录
if not os.path.exists('avatars'):
    os.makedirs('avatars')

def download_avatar(row):
    avatar_url = row['头像']
    user_id = row['id']
    try:
        response = requests.get(avatar_url, stream=True)
        if response.status_code == 200:
            # 确定文件扩展名
            ext = os.path.splitext(avatar_url)[1] if os.path.splitext(avatar_url)[1] else '.avif'
            file_path = f'avatars/{user_id}{ext}'
            with open(file_path, 'wb') as out_file:
                for chunk in response.iter_content(chunk_size=128):
                    out_file.write(chunk)
            return f'Successfully downloaded {file_path}'
        else:
            return f'Failed to download {avatar_url}'
    except Exception as e:
        return f'Error downloading {avatar_url}: {e}'

# 使用ThreadPoolExecutor进行多线程下载
with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(download_avatar, row) for index, row in df.iterrows()]
    for future in as_completed(futures):
        print(future.result())
