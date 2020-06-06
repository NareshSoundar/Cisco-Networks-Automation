from getpass import getpass
from pip._vendor.distlib.compat import raw_input
from netmiko import ConnectHandler
from datetime import datetime

host = input('Enter ip address : ')
username  = input('Enter username ')
password = input('Ente password')

start_time = datetime.now()
print(start_time)

iosv_l2_s1 = {
        'device_type': 'cisco_ios',
        'ip': host,
        'username': username,
        'password': password,
    }
def version():

    with open(r'F:\Users\pla\PycharmProjects\ssh\venv\showcommands.txt', 'r') as f:
         commands = f.read().splitlines()

         for list in commands:
            print ('Connecting to device" ' + list)
            net_connect = ConnectHandler(**iosv_l2_s1)
            output = net_connect.send_command(list)
            with open(r'F:\Users\pla\PycharmProjects\ssh\venv\showcommandoutput.txt', 'a') as f:
                    f.write(output)
                    f.write("\n---------------------------------------------------end--------------------------------------------------")
                    print(output)
version()
end_time = datetime.now()
print(end_time)
total_time = end_time - start_time
print(total_time )
