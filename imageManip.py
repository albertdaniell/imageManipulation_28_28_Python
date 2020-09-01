from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv

#open image using PIL
im = Image.open("images/img1.jpg")


#resize the image

resized_im=im.resize((28,28)).convert('L')


#convert image to grayscale

im_converted_gray=im.resize((28,28)).convert('L')


plt.imshow(np.array(resized_im))
plt.show()
print(np.array(resized_im))




# print(im_converted_gray.shape)
# gr_im= Image.fromarray(im_converted_gray).save('./images/leg.png')
# with open('images_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([np.array(resized_im), "leg",])