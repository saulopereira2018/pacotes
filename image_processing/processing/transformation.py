#Author: Karina Tiemi Kato
from skimage.transform import resize

def resize_image(image, proportion):
#Pega uma imagem e uma proporção, e retorna uma imagem redimensionada
#param image: a imagem a ser redimensionada
#param ratio: A proporção da imagem original para redimensionar
#return: A imagem está sendo redimensionada para a proporção especificada.

    assert 0 <= proportion <=1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0]*proportion)
    width = round(image.shape[1]*proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized