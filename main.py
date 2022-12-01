from operation import ImageOperation
from utils.resize import resize_image


a=ImageOperation("test_image\d41586-020-01430-5_17977554.jpg")
dimension=[(70,70),(80,80),(120,340),(300,300)]

new_images=a.get_resized_image(dimension)
print(new_images)   #To test wheather it's returning right or not

