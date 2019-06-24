#!/usr/bin/env python

import bluetooth, time
import rospy
from std_msgs.msg import String

search_time = 10
addr = None


print("Welcome to the Bluetooth Detection Demo! \nMake sure your desired Bluetooth-capable device is turned on and discoverable.")

if addr == None:
    try:
        input("When you are ready to begin, press the Enter key to continue...")
    except SyntaxError:
        pass

    print("Searching for devices...")

    nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)

    if len(nearby_devices) > 0:
        print("Found %d devices!" % len(nearby_devices))
    else:
        print("No devices found! Please check your Bluetooth device and restart the demo!")
        exit(0)

    i = 0 # Just an incrementer for labeling the list entries
    # Print out a list of all the discovered Bluetooth Devices
    for addr, name in nearby_devices:
        print("%s. %s - %s" % (i, addr, name))
        i =+ 1

    device_num = input("Please specify the number of the device you want to track: ")

    # extract out the useful info on the desired device for use later
    addr, name = nearby_devices[device_num][0], nearby_devices[device_num][1]


server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,addr = server_socket.accept()
print "Accepted connection from ",addr

data=""
while 1:
         data= client_socket.recv(1024)
         print "Received: %s" % data
	 pub = rospy.Publisher('chatter',String , queue_size=1)
         rospy.init_node('talk', anonymous=True)
         # while not rospy.is_shutdown():
         hello_str = "%s" % data
         ##rospy.loginfo(hello_str)
         pub.publish(hello_str)





client_socket.close()
server_socket.close()


