from PIL import Image
from utils.resize import resize_image
import os
from Repository.database import collection

class  ImageOperation:
    def __init__(self, image):
        self.image=image
        

    def get_resized_image(self, dimensions):
        image = Image.open(self.image)
        all_resized_images = []
        
        for i, dim  in enumerate(dimensions):
            resized_image = resize_image(image,dim)
            resized_image_name= os.getcwd()+"\Resized_image\\"+"new"+str(i)+".jpg"
            # print("image path: ",resized_image_name)
            resized_image.save(resized_image_name)
            all_resized_images.append(resized_image_name)
        return all_resized_images



