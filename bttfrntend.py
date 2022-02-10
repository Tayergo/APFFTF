import os
os.system("clear")
print("Hello. this is a python program, mainly as a front-end to basic system stuff.")
print("press 1 for updating packages. press 2 for basic terminal commands.")
val = input()
if(val == "1"):
	os.system("~/sysfunction/update.sh")
elif(val == "2"):
	os.system("~/sysfunction/btt2.sh")