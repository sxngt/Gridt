from data_loader import data_name_to_list
from database.config import URI
from database.conn import mongo
from argparse import ArgumentParser, BooleanOptionalAction
from os import listdir, path

project_home_path = "/Users/ysh/Dev/Python/mitsAI"

if __name__ == "__main__":
    mongo.init_app(uri=URI, port=27017)

    parser = ArgumentParser(description="this is mongoDB GridFS Based large-image-data injector")
    parser.add_argument('--path', "-p", type=str, default="/data", help="You must enter a relative path based on the "
                                                                        "project home directory.")
    parser.add_argument("--database", "-d", type=str, help="Database in MongoDB to store data")
    parser.add_argument("--subdirectory", '-s', action=BooleanOptionalAction, help="If you're going to inject a data "
                                                                                   "folder that has a lot of "
                                                                                   "subdirectories, you can use that "
                                                                                   "option to move all the data in the "
                                                                                   "subdirectories in batches.")

    args = parser.parse_args()

    filename_list = data_name_to_list(project_home_path + args.path)


    def put_files_in_gridfs(folder_path, parent_folder=''):
        for item in listdir(folder_path):
            item_path = path.join(folder_path, item)
            if path.isdir(item_path):
                # 폴더인 경우, 재귀적으로 내부 탐색
                put_files_in_gridfs(item_path,parent_folder=path.join(parent_folder, item).replace('\\', '/'))
            else:
                # 파일인 경우, GridFS에 저장
                with open(item_path, 'rb') as f:
                    uniform_parent_folder = parent_folder.replace('\\', '/')
                    mongo.gfs_upload(f, filename=item, metadata={'folder': uniform_parent_folder})
                    print("upload", item)


    if args.subdirectory:
        mongo.connect(args.database)

        put_files_in_gridfs(project_home_path + "/" + args.path)

        mongo.close()

    else:

        #TODO 해당메소드 고도화 필요
        mongo.connect(args.database)

        for filename in filename_list:
            with open(project_home_path + args.path + "/" + filename, 'rb') as f:
                res = mongo.gfs_upload(f, filename=filename)
                print("upload" + filename + "succeed")

        mongo.close()
