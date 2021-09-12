import data_generator
import numpy as np


x_set = [];
y_set = [];

for p in (1,2,3):
    print(f"Generating p={p}");
    for ttwo in np.linspace(120e-6,600e-6,1000):
        graphset = data_generator.get_graphset(set_p=p,set_ttwo=ttwo);
        x_set.append(graphset[0]);
        y_set.append(graphset[1]);

print("graphsets generated. saving...");


full_dataset = [];
full_dataset.append(x_set);
full_dataset.append(y_set);
full_dataset = np.array(full_dataset);


print(full_dataset)

np.save("ml_dataset",full_dataset)

print("q.e.d.");