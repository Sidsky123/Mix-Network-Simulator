from simulation_modes import test_mode
import os
# from experiments import plotting
from metrics import anonymity_metrics
import pandas as pd
import json
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
# import classes.Node

epsilon_list =[]
delta_list = [] 

EPSILON = 1
DELTA = 1e-4

def main():
     # try:
    entropy=()
    unlinkability=()
    latency=()

    print("Mix-network Simulator\n")
    print("Insert the following network parameters to test: ")

    with open('test_config.json') as json_file:
        config = json.load(json_file)

    if not os.path.exists('./playground_experiment/logs'):
        os.makedirs('./playground_experiment/logs')
    else:
        try:
            os.remove('./playground_experiment/logs/packet_log.csv')
            os.remove('./playground_experiment/logs/last_mix_entropy.csv')
        except:
            pass
    
    test_mode.run(exp_dir='playground_experiment', conf_file=None, conf_dic=config)
    throughput = test_mode.throughput

    packetLogsDir = './playground_experiment/logs/packet_log.csv'
    entropyLogsDir = './playground_experiment/logs/last_mix_entropy.csv'
    packetLogs = pd.read_csv(packetLogsDir, delimiter=';')
    entropyLogs = pd.read_csv(entropyLogsDir, delimiter=';')

    unlinkability = anonymity_metrics.getUnlinkability(packetLogs)
    entropy = anonymity_metrics.getEntropy(entropyLogs, config["misc"]["num_target_packets"])
    latency = anonymity_metrics.computeE2ELatency(packetLogs)
    
    print("\n\n")
    print("Simulation finished. Below, you can check your results.")
    print("-------------------------------------------------------")
    print("-------- Anonymity metrics --------")
    print(">>> Entropy: ", entropy)

    current_no_nodes =  config["network"]["cascade"]["cascade_len"]
    if unlinkability[0] == None:
        epsilon_list.append(15)
        delta_list.append(unlinkability[1])
        print(">>> E2E Unlinkability: epsilon= -, delta=%f)" % unlinkability[1])
    else:
        epsilon_list.append(unlinkability[0])
        delta_list.append(unlinkability[1])
        print(">>> E2E Unlinkability: (epsilon=%f, delta=%f)" % unlinkability)
    print("\n\n")
    print("-------- Performance metrics --------")
    print(">> Overall latency: %f seconds (including mixing delay and packet cryptographic processing)" % (latency))
    print(">> Throuhput of the network: %f [packets / second]" % throughput)
    print("-------------------------------------------------------")
    print("UNlinkability in Playground is " + str(float(unlinkability[0])))

    # report_cumulative_noise()

    with open('values.txt', 'a') as f:
        f.write(str(round(float(unlinkability[0]),4)) + ',')

    return float(unlinkability[0])
    
if __name__ == "__main__":
   main()