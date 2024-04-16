import os
from metrics import anonymity_metrics
import pandas as pd
import json
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from playground import *

mixnodes_list = [3,5,7,9]
unlinkability_list =[]
open("values.txt", "w").close()

for i in mixnodes_list:
    with open('test_config2.json','r') as json_file:
        config = json.load(json_file)
        config["network"]["topology"] = "cascade"
        config["mixnodes"]["avg_delay"] = 0.1
        config["mixnodes"]["batch"] = True
        config["cover_traffic"] = True
        print("done reading 1 2 3")
        config["network"]["cascade"]["cascade_len"] = i
        newData = json.dumps(config)

    with open ('test_config.json', 'w') as file:
        file.write(newData)
    
    current_val = float(os.system('python playground.py'))
    print("Current val is" + str(current_val))


with open ('valueslatency.txt','r') as file:
    latency_list = (file.read().split(','))
latency_list.pop()
print(latency_list)

latency_list = [float(i) for i in latency_list]
plt.plot(mixnodes_list, latency_list, color = 'Green')
plt.xlabel('Number of Mixnodes')
plt.ylabel('Latency')
plt.title("Latency with different number of nodes without DP noise")
plt.savefig('Plots_Cascade_CoverTrafficOn_BatchOn_Unlinkability.png')