import os

from database.conn import mongo
from database.config import URI

if __name__ == "__main__":
    mongo.init_app(uri=URI, port=27017)

    # 싱글턴처럼 사용합시다...

    mongo.connect("testingDB")
    #mongo.gfs_download(output_file_path="/Users/ysh/Dev/Python/mitsAI/download/test.jpg", filename="chest1.jpg")
    data = mongo.gfs_get({"filename": "chest1.jpg"})
    print(data)
    mongo.close()


def data_name_to_list(folder_path: str) -> list:
    file_and_dirs = os.listdir(folder_path)
    return file_and_dirs