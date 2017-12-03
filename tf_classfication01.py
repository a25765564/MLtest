import tensorflow as tf
import skimage
from skimage import data
import os
def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []    
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".ppm")]        
        for f in file_names:
            images.append(data.imread(f))
            labels.append(int(d))    
    return images, labels

ROOT_PATH = "F:\\kaggle\\belgiumTSC"
train_data_directory = os.path.join(ROOT_PATH, "Training")
test_data_directory = os.path.join(ROOT_PATH, "Testing")

images, labels = load_data(train_data_directory)

#print the images dimensions
print(images.ndim)

#print the number of 'images'`s element
print(images.size)

images[0]

#show the plot
import matplotlib.pyplot as plt

plt.hist(labels,62)
plt.show()




