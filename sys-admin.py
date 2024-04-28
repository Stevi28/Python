# using os.system
# import os and subprocess modules
import os
import subprocess

# ls from bash
#os.system('ls')

# using subprocess.run
# you can use it to run any bash command 
#subprocess.run(['ls'])

# using subprocess.run with 2 arguments
#subprocess.run(['ls', '-l'])

# using subprocess.run with 3 arguments
subprocess.run(['ls', '-l', 'README.md'])

# retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

