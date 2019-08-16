import math
import numpy as np

# built up the data from experiments
def builtData(fileName):
    fileobj = open(fileName,'r')
    lines = fileobj.readlines()
    fileobj.close()

    line_count = len(lines)
    exp_count = int(line_count/5) # every experiment has 5 lines of data
    exp = np.zeros((exp_count, 5))
    
    for i in range(line_count):
        exp_ind = int(i/5) # get current experiment id
        ind = i%5 # get every individual data in the experiment
        str1 = lines[i].split(' ')
        if(ind == 0):
            exp[exp_ind][0] = int(str1[2]) # interval value
            exp[exp_ind][1] = int(str1[3]) # dosage volume

        elif(ind == 1):
            exp[exp_ind][2] = int(str1[4]) # time start effect

        elif(ind == 3):
            exp[exp_ind][3] = float(str1[4]) # Maximum post-effective

        elif(ind ==4):
            exp[exp_ind][4] = float(str1[4]) # Average post-effective

    return (exp)

# get the value which is non-zero
def getValueData(data):
    result_list = []
    time_step = []
    max_eff_data = []
    ave_eff_data = []
    for i in range(len(data)):
        eff_time = data[i][2] # time statrt effect
        high_val = data[i][3] # max value
        low_val = data[i][4]  # ave value
        if(high_val != 0):
            exp_name = str(int(data[i][0]))+'-'+str(int(data[i][1]))
            result_list.append(exp_name)
            time_step.append(int(eff_time))
            max_eff_data.append(data[i][3])
            ave_eff_data.append(data[i][4])

    return (result_list, time_step, max_eff_data, ave_eff_data)

# find the fastest effect result
def findBestResult(time_step, result_list):
    best_result = []
    min_time = min(time_step)
    for ind in range(len(time_step)):
        if time_step[ind] == min_time:
            best_result.append(result_list[ind])
    return min_time, best_result
