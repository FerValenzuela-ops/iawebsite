
"""
Created on Thu Jan 13 17:42:38 2022

@author: Ferna
"""
import PIL.Image
from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array, load_img

Y = 'Gato'
X = 'Perro'


sample_y_image = 'D:/spyderDev/train/y/00000001.jpg'

data_gen = ImageDataGenerator(rotation_range=40, width_shift_range=0.2, 
                              height_shift_range=0.2, rescale=(1/255),
                              shear_range=0.2, zoom_range=0.2,
                              horizontal_flip=(True),
                              fill_mode='nearest')

img = load_img(sample_y_image)

x = img_to_array(img)
x = x.reshape((1,) + x.shape)


i = 0

for bach in data_gen.flow(x, batch_size=1, save_to_dir='./preview',
                          save_prefix=y,save_format='jpeg'):

    i += 1
    
    if i > 20:
        break
