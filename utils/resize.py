from PIL import Image
def resize_image(image,dim):
    r=image.resize(dim)
    print(r.show())
    return r
