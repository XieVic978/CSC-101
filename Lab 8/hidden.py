from group import *
from data import*
'''
input: filename
output: Header and list of pixel
purpose: To read the file and then split to take header and list of pixels
'''
def read_ppm_file(filename:str)-> tuple[Header, list[Pixel]]:
    with open(filename,'r') as f:
        file = f.read()
        newfile = file.split()

        header = newfile[1:4] # [500, 375, 255]
        width = int(header[0])
        height = int(header[1])
        max_color = int(header[2])
        newHeader = Header(width,height,max_color)

        data = [int(x) for x in newfile[4:]]
        pixelList = []
        for sublist in groups_of_3(data):
            red = int(sublist[0])
            green = int(sublist[1])
            blue = int(sublist[2])
            pixelList.append(Pixel(red,green,blue))
        return newHeader, pixelList

'''
input: list of pixels
output: list of pixels
purpose: to update the list of pixels so that u increase the value of red by a multiplier of 10 and if it goes above 255
put the value of red to 255, if not then just multiply by 10 and that is the new red value. The green and blue value will
be the same as the new red value

'''

def process_data(lst:list[Pixel])->list[Pixel]:
    newList = []
    for line in lst:
        newRed = line.red * 10
        if newRed >= 255:
            newRed = 255
        newGreen = newRed
        newBlue = newRed
        newList.append(Pixel(newRed,newGreen,newBlue))
    return newList

'''
input: header object and list of pixel
output: a new file 
purpose: to create a new file that has the header, and the new list of pixels

'''

def create_ppm_file(header:Header, lst:list[Pixel]):

    with open('discovered.ppm','w') as f:
        f.write('P3\n')
        f.write(str(header.width) + ' ')
        f.write(str(header.height)+'\n')
        f.write(str(header.max_color) +'\n')

        for color in lst:
            red = color.red
            green = color.green
            blue = color.blue
            f.write(f'{red} {green} {blue}\n')





if __name__ == '__main__':
    header, pixels = read_ppm_file('hidden.ppm')
    print(header)
    print(pixels[:4])
    processed_pixels = process_data(pixels)
    create_ppm_file(header, processed_pixels)


