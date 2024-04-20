import base64
import codecs
from os import listdir, path
from domain.mongo.conn import mongo


def put_files_in_gridfs(folder_path, parent_folder=''):
    for item in listdir(folder_path):
        item_path = path.join(folder_path, item)
        if path.isdir(item_path):
            # 폴더인 경우, 재귀적으로 내부 탐색
            put_files_in_gridfs(item_path, parent_folder=path.join(parent_folder, item))
        else:
            # 파일인 경우, GridFS에 저장
            with open(item_path, 'rb') as f:
                mongo.gfs_upload(f, filename=item, metadata={'folder': parent_folder})
                print("upload", item)


def get_one_image_file_by_filename(filename: str):
    mongo.connect("testingDB")
    file_index = mongo.find(coll_name="fs.files", filter={"filename": filename}, projection={"_id": 1})["_id"]
    data = mongo.gfs_get(file_index)
    base64_data = codecs.encode(data.read(), 'base64').decode('utf-8')

    print(base64_data)
    return {"file_index": str(file_index), "base64_data": base64_data}


def get_id_list(database: str) -> list:
    mongo.connect(database)
    coll = mongo.db.get_collection('fs.files')
    id_list = []
    for document in coll.find({}, {'_id': 1}):  # _id 필드만 조회
        id_list.append(document['_id'])
    return id_list


def get_file_by__id_list(database: str, _id_list: list):
    get_id_list(database)  # 해당 로직에서 mongo.connect 작동함
    base64_list = []
    for _id in _id_list:
        base64_list.append(mongo.gfs_get(_id))
    print(base64_list)