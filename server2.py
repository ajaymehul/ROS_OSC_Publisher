#!/usr/bin/env python

import liblo, sys
import rospy
from std_msgs.msg import String


# create server, listening on port 1234
try:
    server = liblo.Server(12346)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

def foo_bar_callback(path, args,types,src):
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    mes = str(args[0])
    pub.publish(mes)
   

# register method taking an int and a float
server.add_method("/openbci/focus", None, foo_bar_callback)


# loop and dispatch messages every 100ms
while True:
    server.recv(100)

