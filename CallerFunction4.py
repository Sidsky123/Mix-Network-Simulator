import os
from metrics import anonymity_metrics
import pandas as pd
import json
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from playground import *

mixnodes_list = [1,3,5,7,9,10]
unlinkability_list =[]
open("values.txt", "w").close()

for i in mixnodes_list:
    with open('test_config2.json','r') as json_file:
        config = json.load(json_file)
        config["network"]["topology"] = "stratified"
        print("done reading 1 2 3")
        config["network"]["stratified"]["layers"] = i
        newData = json.dumps(config)

    with open ('test_config.json', 'w') as file:
        file.write(newData)
    
    current_val = float(os.system('python playground.py'))
    print("Current val is" + str(current_val))


with open ('values.txt','r') as file:
    unlinkability_list = (file.read().split(','))
unlinkability_list.pop()
print(unlinkability_list)

unlinkability_list = [float(i) for i in unlinkability_list]
plt.plot(mixnodes_list, unlinkability_list, color = 'Red')
plt.xlabel('Number of Mixnodes')
plt.ylabel('Epsilon')
plt.savefig('Plots.png')