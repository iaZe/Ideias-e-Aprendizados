#!/usr/bin/python3
# coding: utf-8

import sys
import socket

def portScan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return True
    except:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 portScan.py <host> <port>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    if portScan(host, port):
        print("Port %d is open" % port)
    else:
        print("Port %d is closed" % port)
