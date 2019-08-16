#!/bin/bash
echo Which drug you want to simulate?
echo Enter 1 for niLess
echo Enter 2 for Polyjuice
echo
echo Pleace enter the number:

# let user select the a drug to simulate
controler=0
while [ $controler = 0 ] ;do
	read getval
	
	# setup variables when user select a drug
	if [ $getval = 1 ]; then
		controler=1
		drug=niLess
		MEC=80
		MTC=140
		h_life=42
		af=0.42
	elif [ $getval = 2 ]; then
		controler=1
		drug=Polyjuice
		MEC=50
		MTC=66
		h_life=9.95
		af=0.14
	# ask again if user type an incurrent selection
	else
		echo Incorrect input
		echo select again: 1 = niLess, 2 = Polyjuice
	fi
done
echo you select $drug
echo
echo start simulating...
echo

cd code

count=0 # check whether it is a first time input result
outfile="../result/$drug/result.txt"

for i in `seq 1 1 24`;
do
	for d in `seq 10 10 1000`;
	do
		echo "Experiment: "$i $d

		if [ "$count" = 0 ];then
			count=1
			echo "Experiment: " $i $d > $outfile
		else
			echo "Experiment: " $i $d >> $outfile
		fi

		python3 dosagetest.py $i $d $h_life $MEC $MTC $af >> $outfile
	done
done
echo
echo Complete Simulation
echo
echo Start Analysing data...
echo

readfile="$outfile"
outResult="../result/$drug/graph/"
python3 data_analyser.py $readfile $outResult
echo
echo Complete!
