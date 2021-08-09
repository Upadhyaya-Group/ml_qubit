import data_generator
import numpy as np


list_size = 20;
x_set = [];
y_set = [];

ttwonaught = 343e-6;
for i in range(0,100):
    graphset = data_generator.get_graphset(1,(ttwonaught) * i**2 * 0.5);
    x_set.append(graphset[0]);
    y_set.append(graphset[1]);

full_dataset = [];
full_dataset.append(x_set);
full_dataset.append(y_set);
full_dataset = np.array(full_dataset);


print(full_dataset)

np.save("ml_dataset",full_dataset)