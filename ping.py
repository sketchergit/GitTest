import os

y = 0

def ping(ip):
    x = os.popen('ping -c 4 ' + ip).read()
    if '64 bytes' in x:
        y = 'UP'
    else:
        y = 'DOWN'
    return y
'''
ip = input("Enter IP address: ")
print(ping(ip))
'''

