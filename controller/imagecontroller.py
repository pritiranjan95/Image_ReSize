from fastapi import FastAPI,APIRouter, UploadFile,Form,File
from service.operation import ImageOperation
from model.imagemodel import ImageModel, Dimension
import json
from Repository.database import collection

router=APIRouter()

@router.get("/")
def homepage():
    return "Hi this is the home page, Go to docs to find the information about this api"


@router.post("/upload",name="image controller post",tags=["image"])
def modelshow(image:UploadFile, imagemodel:ImageModel):

    a=ImageOperation(image.file)
    new_images=a.get_resized_image(imagemodel.dimension)
    return new_images
#The above didn't work as we use form and json objects together.

@router.post('/file',name="image controller post",tags=["image"])
def _file_upload(image: UploadFile, image_dimentions: str):

    image_dimentions = json.loads(image_dimentions) #json.load() use change the string to a json object, here we got it from the user as a stirng. Json object can be a list also.
    a=ImageOperation(image.file)
    new_images=a.get_resized_image(image_dimentions)
    return new_images



