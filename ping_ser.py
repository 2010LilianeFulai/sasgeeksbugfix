mport od
import platform
iport subprocess
import sys

def ping_server(server):
Determine the command based on the OS
param = ['-n' platform.system().lower == 'window' else '-c'
command = ['ping',param,'4',sever] #Ping 4 times

try:
Execute the command
  output  subprocess.check_output(command,stdrr=subprocess.STDOUT,universal_newlines=True)
  print(f"Ping Output:\n{e.output})

if name--"main":
   if len(sys.argv) !=2:
print('Usage: python ping_server.py")
sys.exit(1)

   server_toping =sys.argv[1]
   ping_server(server_to_ping)
