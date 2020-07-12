#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import glob
import datetime
import tarfile
import urllib.request


# In[ ]:


# creating a main function which takes information about the path to the training and unsorted dataset 
if __name__ == '__main__':
    
  train_dir = "C:/Users/nitin/OneDrive/Desktop/CourseWork/Python/"
# If no directory is found, make one!
  if not os.path.exists(train_dir):
    os.makedirs(train_dir)
  if os.path.exists(train_dir + "\\train"):
    os.rename(train_dir + "\\train", train_dir + "\\train")


# In[ ]:


# define
  # get the class label limit
  class_limit = 12

  # take all the images from the dataset
  image_paths = glob.glob(train_dir + "\\train\\*.png")

  # variables to keep track
  label = 0
  i = 0
  j = 150

  # plant_seedling_classification (12 classes) class names
  class_names = ["black_grass", "charlock", "cleavers", "common_chickweed", "common_wheat",
             "fat_hen", "loose_silky_bent", "maize", "scentless_mayweed", "shepherds_purse", 
             "small_flowered_cranesbill", "sugar_beet"]

  # loop over the class labels
  for x in range(1, class_limit+1):
    # create a folder for that class
    os.makedirs(train_dir + "\\train\\" + class_names[label])
    
    # get the current path
    cur_path = train_dir + "\\train\\" + class_names[label] + "\\"
    
    # loop over the images in the dataset
    for index, image_path in enumerate(image_paths[i:j], start=1):
      original_path   = image_path
      image_path      = image_path.split("\\")
      image_file_name = str(index) + ".png"
      os.rename(original_path, cur_path + image_file_name)
    
    i += 150
    j += 150
    label += 1

