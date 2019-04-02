# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


#Import necessary modules
import subprocess
import time
import sys

def resulter():
	command = ("iwconfig wlp1s0")

	proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

	(out, err) = proc.communicate()
	pos = out.find("Link".encode())
	result = int(out[pos+13:pos+15])
	result = (round((int(result) / 70)*100))
	return(result)

#main function to run the command and parse the information to give the output of Link strength.
def normal():
	print('Determing average strength...')
	values = []
	for i in range(500):#set to 500
		result = resulter()
		time.sleep(0.01)
		values.append(result)
	average = round(sum(values)/len(values))
	print('Average: '+str(average)+ '%')
	return(average)

def sensitivity():
	try:
		sensitivity = 10 - (int(sys.argv[1]))
	except:
		print('Using default sensitivity of 8 (can be adjusted on a scale of 1-10 with 1 being lowest sensitivity)')
		sensitivity = 2
	return(sensitivity)

def main():
	sens = sensitivity()
	average = normal()
	while True:
		currentsig = resulter()
		if (currentsig > average + sens) or (currentsig < average - sens):
			sys.stdout.write('\rMovement Detected with '+str(currentsig)+'%    ')
			#print('Movement Detected')
		else:
			sys.stdout.write('\rNo Movement Detected            ')

main()
