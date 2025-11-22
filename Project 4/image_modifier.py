from data_image import *

def read_image(file:str) -> tuple[Header, list[str]]:

    with open(file,'r') as file:
        newFile = file.read().split()
        header = newFile[1:4]
        width = int(header[0])
        height = int(header[1])
        max_color = int(header[2])
        newHeader = Header(width,height,max_color)
        pixels = newFile[4:]

        return newHeader, pixels

def create_objects(pixel:list[str])->list[Pixel]:
    newList = []
    for idx in range(0, len(pixel), 3):
        red = int(pixel[idx])
        green = int(pixel[idx + 1])
        blue = int(pixel[idx + 2])
        newList.append(Pixel(red, green, blue))
    return newList


def negate(lst:list[Pixel]):
    newList = []
    for color in lst:
        red = abs(color.red - 255)
        green = abs(color.green - 255)
        blue = abs(color.blue - 255)
        newList.append(Pixel(red, green, blue))
    return newList

def high_contrast(lst:list[Pixel]):
    newList = []
    for color in lst:
        red = color.red
        green = color.green
        blue = color.blue
        red = 255 if red > 127 else 0
        green = 255 if green > 127 else 0
        blue = 255 if blue > 127 else 0
        newList.append(Pixel(red, green, blue))
    return newList

def gray_scale(lst:list[Pixel])->list[Pixel]:
    newList = []
    for color in lst:
        red = color.red
        green = color.green
        blue = color.blue
        average = (red + green + blue) // 3
        nRed = average
        nGreen = average
        nBlue = average
        newList.append(Pixel(nRed,nGreen,nBlue))
    return newList


def remove_color(lst:list[Pixel], color)->list[Pixel]:
    newList = []

    for line in lst:
        red = line.red
        green = line.green
        blue = line.blue
        if color == 'red':
            red = 0
        elif color == 'green':
            green = 0
        else:
            blue = 0
        newList.append(Pixel(red,green,blue))
    return newList


def write_file(header:Header, lst:list[Pixel],output):
    pass