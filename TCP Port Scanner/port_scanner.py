import socket

common_ports = [22,23,25,53,80,139,443,3386,3389,445]

def custom_scan(ip):
    
    for i in range(25):
        s = socket.socket()
        r = s.connect_ex((ip,i))
        check(r,i)

def common_scan(ip):
    for i in common_ports:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        r = s.connect_ex((ip,i))
        check(r,i)

def check(r,i):
    if r == 0:
        print('port',i,'is open')
    else:
        print('port',i,'is closed')
def menu():
    print('Port Scanner'.center(50,'*'))
    print('\nchoose scanning method')
    print('1. first 1000 scan')
    print('2. 10 common scan\n')
    print(''.center(50,'*'))

menu()

choice = input('select number : ')

ip = input("ip address: ")

if choice == str(1):
    custom_scan(ip)
elif choice == str(2):
    common_scan(ip)