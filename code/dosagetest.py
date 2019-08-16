#
# repeatdosage.py
#
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

# print everything zero if it is a valueless result
def badResult():
    print('Effective at : \t', 0)
    print('Minimum post-effective value: \t', 0)
    print('Maximum post-effective value: \t', 0)
    print('Average post-effective value: \t', 0)


interval = int(sys.argv[1])      # hours between doses
dosage = int(sys.argv[2])*1000     # dosage 
half_life = float(sys.argv[3])            # Dilantin half-life
MEC = float(sys.argv[4])                 # Effective concentration
MTC = float(sys.argv[5])                # Toxic concentration
absorption_fraction = float(sys.argv[6])

volume = 3000             # blood plasma volume
drug_in_system = 0        # initial amount of drug in system
ln05 = math.log(0.5)
elimination_constant = -ln05/half_life
pulse = 0
entering = absorption_fraction * pulse * dosage
elimination = elimination_constant * drug_in_system
concentration = drug_in_system/volume

simulation_time = 720     # simulation time 168
time_step_size = 1        # time step = 1 hour
num_steps = int(simulation_time/time_step_size)
cumulative_time = 0.0     # initial time = 0

values = np.empty(num_steps) 

for time_step in range (num_steps):
    values[time_step] = concentration
    if (time_step % interval == 0):
       pulse = 1
    else:
       pulse = 0
    entering = absorption_fraction * pulse * dosage
    elimination = elimination_constant * drug_in_system
    drug_in_system = drug_in_system - elimination + entering
    concentration = drug_in_system / volume

times = np.linspace(0, simulation_time - time_step_size, num_steps)

# detect the start effect time
effective = 0
while effective < len(values) and values[effective] < MEC :
    effective += 1

# check Whether medician effect during the entire time frame
if (effective < len(values)):
    stable_max_val = values[effective:].max()
    stable_min_val = values[-10:-1].min()
    
    # print the result when the maximun and minimun value is in the effect area
    # print 0 otherwise.
    if(stable_max_val < MTC and stable_min_val > MEC):
        print('Effective at : \t', effective)
        print('Minimum post-effective value: \t', values[effective:].min())
        print('Maximum post-effective value: \t', values[effective:].max())
        print('Average post-effective value: \t', values[effective:].mean())

        '''
        # Below show the graph of what do the good result look like
        MECline = np.full(num_steps, MEC)
        MTCline = np.full(num_steps, MTC)
        baseline = np.full(num_steps, stable_min_val)
        plt.figure()
        plt.title('Dilantin Concentration')
        plt.xlabel('Time (hours)')
        plt.ylabel('Concentration')
        plt.plot(times, values, '-', times, MECline, 'g-', times, MTCline, 'r-', times, baseline, 'b--')
        plt.savefig('test/dosage_' + 'I' + str(Vinterval)+'_D' + str(Vdosage) + '.png')
        '''
    else:
        badResult()
else:
    badResult()
