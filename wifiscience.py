# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


#written for my grade 10 science expo project

#Import necessary modules
import subprocess
import time

#set variables and list
material = raw_input("What material are you testing? ")
list1 =[]
numtimes = int(raw_input("Number of times to test?: "))

#main function to run the command and parse the information to give the output of Link strength.
def results():
	for i in range(numtimes):
		num = 1
		command = ("iwconfig wlp1s0")

		proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)

		(out, err) = proc.communicate()	
		pos = out.find("Link")
		global result
		result = out[pos+13:pos+18]
		list1.append(result)
		print (result)
		time.sleep(0)

def write():
	f = open(material+".txt", "w")
	f.write("Material tested: "+material+"\n")
	for i in range(numtimes):
		f.write(list1[i]+"\n")
	
	f.close()	
	
	
	
# main function to run results and add it all to a txt file with the name of the material tested as the files name and included inside the program.
def main():
	results()
	print(list1)
	write()
	
	
#to run the program
main()


