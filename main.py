from operation import ImageOperation
from utils.resize import resize_image
from fastapi import FastAPI, APIRouter

from controller import imagecontroller

#For testing we can use the below one.    

# a=ImageOperation("test_image\d41586-020-01430-5_17977554.jpg")
# dimension=[(70,70),(80,80),(120,340),(300,300)]
# new_images=a.get_resized_image(dimension) #the function has defined in the class operation.
# print(new_images)  #To test wheather it's returning right or not.



#Now do it in api, Take the data from the user.

app=FastAPI()
app.include_router(imagecontroller.router)
