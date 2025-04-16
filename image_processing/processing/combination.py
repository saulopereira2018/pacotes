#Author: Karina Tiemi Kato
import numpy as np
from skimage.color import rgh2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    """
    Ele pega duas imagens, as converte em escala de cinza, calcula o índice de similaridade estrutural e retorna uma imagem de diferença normalizada
     :param image1: A primeira imagem a comparar
     :param image2: A imagem para comparar
     :return: A imagem de diferença normalizada.
    """
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histrogram(image1, image2):
    """
    Recebe duas imagens como entrada e retorna uma nova imagem com o histograma da primeira imagem correspondida para o histograma da segunda imagem
    
     :param image1: A imagem que você deseja combinar com o histograma de
     :param image2: A imagem para a qual queremos transferir o histograma da image1
     :return: A imagem correspondente está sendo retornada.
    """
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image