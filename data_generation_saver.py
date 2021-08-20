import data_generator
import numpy as np


list_size = 20;
x_set = [];
y_set = [];

#ttwonaught = 343e-6;
for ttwo in np.linspace(120e-6,600e-6,302):
    graphset = data_generator.get_graphset(1,ttwo);
    x_set.append(graphset[0]);
    y_set.append(graphset[1]);


def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = np.max(arr) - np.min(arr)    
    for i in arr:
        temp = (((i - np.min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr
  
'''
x_set = normalize(x_set,0,1);

y_set = normalize(y_set,0,1);
'''

full_dataset = [];
full_dataset.append(x_set);
full_dataset.append(y_set);
full_dataset = np.array(full_dataset);


print(full_dataset)

np.save("ml_dataset",full_dataset)