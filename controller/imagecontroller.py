from fastapi import FastAPI,APIRouter, UploadFile
from utils.resize import resize_image
from  operation import ImageOperation

router=APIRouter()

@router.post("/home/")
def show(image: UploadFile,dim:str | None=None ):

    # a=ImageOperation(image.filename)
    # new_image=a.get_resized_image(dimention)
    return {"file name":image.filename}

    