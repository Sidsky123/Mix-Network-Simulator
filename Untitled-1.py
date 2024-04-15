# from tkinter import *
# import tkinter as tk
# import json
# import os

# cwd = os.getcwd()
# path = cwd + "\Simulator-main"
# os.chdir(path)
# cwd = os.getcwd()
# print(cwd)

# win = tk.Tk()
# win.title('Data Entry for Simulator')
# win.geometry("800x600")
# win.columnconfigure((0,1),weight =1)
# win.rowconfigure(0, weight = 1)
# win.rowconfigure((1,2,3,4,5,6), weight = 2)

# label = Label (win,text="Getting Values for simulation", font = ("Calibri 14"))
# # label.pack()
# label.grid(row = 0, columnspan=2, sticky = N)

# network_type = ["P2P","Stratified","Cascade","Multi_Cascade"]
# network_val = StringVar(win) 

# network_val.set("Select a value")
# label_network = Label (win,text="Getting Values for Network Type", font = ("Calibri 10"))
# network_menu = OptionMenu(win, network_val, *network_type)

# label_network.grid(column =0, row =1)
# network_menu.grid(column =1,row =1, sticky = W+E) #column_span is removed

# def submit_callback():
#     get_values()

# submit_button = Button(text="Submit", width = 10, command= submit_callback)
# submit_button.grid(row=6,columnspan=2)
# # network_menu.pack()
# def get_values():
#     chosen_opts=[]
#     # self.network_type_inp= network_type_inp
#     # chosen_opts.add(network_type_inp_)
#     # modify_values(network_type_inp_)
    
#     with open('test_config2.json','r') as json_file:
#         config = json.load(json_file)
#         config["network"]["topology"] = network_val.get()
#         print("done reading 1 2 3")
#         newData = json.dumps(config)

#     with open ('test_config.json', 'w') as file:
#         file.write(newData)

# # def modify_values(self, net):
# #     self.net = net
# win.mainloop()
