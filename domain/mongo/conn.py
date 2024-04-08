import pymongo.database
from gridfs import GridFS, GridFSBucket


class MongoDB:
    def __init__(self):
        self.conn = None
        self.db: pymongo.database.Database = pymongo.Database
        self.uri = None
        self.port = None

        self.db_name = None
        self.coll_name = None

    def __del__(self):
        if self.conn is not None:
            self.close()

    def init_app(self, uri, port):
        self.conn = pymongo.MongoClient(
            host=uri,
            port=port,
            document_class=dict,
            tz_aware=False,
            connect=True
        )

    def connect(self, db_name=None):
        if db_name is None:
            raise AttributeError("db_name is not allow")

        self.db_name = db_name

        self.db = self.conn.get_database(self.db_name)

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def find(self, coll_name: str, filter, projection=None, skip=0, limit=30, sort=None):
        coll = self.db.get_collection(coll_name)
        result = coll.find(filter=filter, projection=projection, skip=skip, limit=limit, sort=sort)
        return result

    def find_all(self, coll_name):
        coll = self.db.get_collection(coll_name)
        result = coll.find({})
        return result

    def gfs_upload(self, data, filename, metadata):
        gfs = GridFS(self.db)
        data = data
        insert_image = gfs.put(data, filename=filename, metadata=metadata)
        return insert_image

    def gfs_get(self, filter):
        gfs = GridFS(self.db)
        data = gfs.find(filter)
        return data

    def gfs_download(self, output_file_path, filename):
        gfs = GridFSBucket(self.db)
        with open(output_file_path, "wb") as output_file:
            gfs.download_to_stream_by_name(filename=filename, destination=output_file)
        print("download {0}".format(filename))


mongo = MongoDB()
