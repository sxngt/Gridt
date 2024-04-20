from fastapi import APIRouter, UploadFile
from domain.file_system import file_system_service

router = APIRouter(
    prefix="/file"
)


@router.post("/one")
async def one_file_upload(file: UploadFile):
    print(file)
    return 0


@router.post("/many")
async def many_file_upload():
    return 0


@router.get("/one/image")
async def get_one_image_file_by_filename(filename):
    return file_system_service.get_one_image_file_by_filename(filename)


@router.get("/id")
async def get_db_index(database):
    return file_system_service.get_id_list(database)

@router.get("/many")
async def get_many_file_by_database_name(database):
    _id_list = file_system_service.get_id_list(database)
    return file_system_service.get_file_by__id_list(database, _id_list)
