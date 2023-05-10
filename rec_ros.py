#!/usr/bin/env python 
import socket
print("started")
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
import rospy
from std_msgs.msg import String

def udp_callback(data):
	rospy.loginfo("received message: %s", data.data)

def main():
	rospy.init_node("udp_listener")
	udp_sub = rospy.Subscriber("udp_messages", String, udp_callback)
	rospy.spin()

if __name__ == "__main__":
	main()
