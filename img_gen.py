from PIL import Image 
import os
import glob
import random

def collage():
    if not os.path.isdir('images'):
        print('You need to generate images')
        return
    
    im = Image.new('RGB', (1000, 1000), 'black')    

    f_list = glob.glob('images/*.jpg')
    random.shuffle(f_list)
    #print(f_list[:4])
    
    idx_list = range(10, 110, 10)
    row_list = range(0, 1000, 100)

    for row, idx in zip(row_list, idx_list) :
        for n, item in zip(range(0, 1100, 100), f_list[idx-10:idx]):
            with Image.open(item) as file: 
                im.paste(file,(n, row))   
    im.show()



if __name__ == '__main__':
    collage()
