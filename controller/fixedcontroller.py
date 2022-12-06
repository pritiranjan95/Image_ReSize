from model.imagemodel import Dimension
from Repository.database import collection
from fastapi import FastAPI,APIRouter, UploadFile
from service.operation import ImageOperation
from bson.json_util import dumps
import json
from service.dataoperation import add, show

router=APIRouter()

@router.post("/fixed-size",name="image Property get",tags=["image Property"])
def dimention(dim:Dimension):
    a=add(dim)
    return a


@router.post("/dim-data",name="image Property get",tags=["image Property"])
def show_image(image:UploadFile):
    sizes=show()
    # print(sizes)
    sizes=sizes[0]["dimension"] #To catch the dimension of the first data of all the datas inside the database.
    
    a=ImageOperation(image.file)
    new_images=a.get_resized_image(sizes)
    return new_images
