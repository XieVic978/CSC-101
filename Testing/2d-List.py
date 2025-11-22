from data_image import *

def read_image(file:str) -> tuple[Header, list[Pixel]]:

    with open(file,'r') as file:
        newFile = file.read().split()
        header = newFile[0:4]
        pixels = newFile[4:]