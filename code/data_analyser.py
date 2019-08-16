import numpy as np
import matplotlib.pyplot as plt
import sys
from funcList import *

data_index = 0
source = sys.argv[1]
path = sys.argv[2]

# Built up data
exp = builtData(source)

# generate valuable data #
result_list,time_step, max_eff_data, ave_eff_data= getValueData(exp)

# Display Bar Chart 
res_list_len = len(result_list)
index = 0
ran = 15   # set the maximun data which print in one graph
count = 1  # the index of output file

while index < res_list_len:
    
    # setup the index data for the output
    if(index+ran < res_list_len):
        stop = index+ran
        ind = np.arange(ran)
    else:
        ind = np.arange(res_list_len - index)
        stop = res_list_len
    
    # display the data
    fig, ax = plt.subplots()
    plt.barh(ind, time_step[index:stop])
    ax.set_yticks(ind)
    ax.set_yticklabels(result_list[index:stop])
    for i, v in enumerate(time_step[index:stop]):
        ax.text(v + 1, i, str(v), color = 'blue')
    ax.invert_yaxis()
    ax.set_ylabel('interval-dosage')
    ax.set_xlabel('Time start effect (hours)')
    plt.savefig(path+'data'+str(count)+'.png')
    plt.clf()

    index = index +ran
    count = count + 1

# Print the best result
if len(time_step)>0:
    min_time, best_result = findBestResult(time_step, result_list)

    for result in best_result:
        print('the best interval-dosage is ', result,',start effect after ',min_time,' hour')
else:
    print('No data match the requirement')
