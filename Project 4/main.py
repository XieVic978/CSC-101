from image_modifier import *

def main():
   header, data = read_image('flower.ppm')
   createobjects = create_objects(data)
   return createobjects


if __name__ == '__main__':
    print(main())