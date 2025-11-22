from hidden import *

def negate(lst:list[Pixel])->list[Pixel]:
    newList = []
    for color in lst:
        red = abs( color.red - 255)
        green = abs( color.green - 255)
        blue = abs( color.blue - 255)
        newList.append(Pixel(red,green,blue))
    return newList

def high_contrast(lst:list[Pixel])->list[Pixel]:
    newList = []
    for color in lst:
        red = color.red
        green = color.green
        blue = color.blue
        red = 255 if red > 127 else 0
        green = 255 if green > 127 else 0
        blue = 255 if blue > 127 else 0
        newList.append(Pixel(red,green,blue))
    return newList


if __name__== "__main__":
    header, data = read_ppm_file('ny.ppm')
    negate_data = negate(data)
    high_contrast_data = high_contrast(data)
    create_ppm_file(header,negate_data)
    #create_ppm_file(header,high_contrast_data)


