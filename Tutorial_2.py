
# coding: utf-8

# # Tutorial 2: Reading all files for the same segment
# In the first tutorial, you learned how to explore one file in the training dataset and plot it. You should have explored some files and now you know what type of data we have. In this tutorial you will learn how to read all files of the same segment into a single dataframe.
# 
# We know that each segment has 4 files, one for each sensor. So we will get all files in one folder, and then read the files of the same segment in the other folders.  

# In[16]:


import pandas as pd
import glob
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

data_folder = 'right_arm/*.csv' 
files = glob.glob(data_folder)


# In[17]:


print(files[1:10])


# As you can see, each file contains the folder and file name. We will keep only the file name

# In[18]:


files = list(map(lambda x: x[x.find("/"):], files))


# In[19]:


print(files[1:10])


# In[22]:


folders = ['right_arm', 'left_wrist', 'left_hip', 'right_wrist']


# For each file name, we will read the data in each folder and create a single dataframe for the whole data. In the next example, we read only three files and plot them. You can see that the columns are renamed to include the name of the sensor body location.

# In[28]:


indices = np.random.randint(low=0, high=len(files), size=4) #get three random numbers
print(indices)
for index in indices:
    all_sensor_data = []
    for folder in folders:
        data = pd.read_csv(folder+files[index])
        data.columns = [folder+"_X", folder+"_Y",folder+"_Z"]
        all_sensor_data.append(data)
    file_data = pd.concat(all_sensor_data, axis=1)
    file_data.plot(subplots=True)


# DO you notice that the right arm and left hip have a shorter graph than the left and right wrist graphs? It is because of the difference in the sampling rate. If you plan to create shorter windows, don't forget this difference! They have the same recording time but with very different sampling rates.  
# 
# 
# To read all data, we will store it in a dictionary using the file name as the key. Remember you need the file name to access the labels! 

# In[29]:


all_data_dict = {}
for file in files:
    all_sensor_data = []
    for folder in folders:
        data = pd.read_csv(folder+file)
        data.columns = [folder+"_X", folder+"_Y",folder+"_Z"]
        all_sensor_data.append(data)
    file_data = pd.concat(all_sensor_data, axis=1)
    all_data_dict[file]=file_data


# # Your turn 
# - Try to get the label for each segment and include it as a new column
# - Try to create some features for each segment, for example the mean, maximum or minimum value of each column
