from pydantic import BaseModel
from fastapi import UploadFile
from typing import List,Set ,Tuple
class ImageModel(BaseModel):
    dimension: List


class Dimension(BaseModel):
    dimension=[[450,300],[500,500],[400,400],[567,567]]

