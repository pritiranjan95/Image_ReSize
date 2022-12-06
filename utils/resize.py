from PIL import Image
def resize_image(image,dim):
    dim=tuple(dim)
    r=image.resize(dim)
    print(r.show())
    return r
