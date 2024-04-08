from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/file/upload"
)


@router.post("/one")
async def one_file_upload(file: UploadFile):
    print(file)
    return 0


@router.post("/many")
async def many_file_upload():
    return 0
