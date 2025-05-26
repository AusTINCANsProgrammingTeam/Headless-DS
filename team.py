#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Headless Driving Station
   Enables Headless Driver Station on FRC robots with 
   ethernet connection
"""

import netifaces

def main():
    ifaddresses = netifaces.ifaddresses('eth0')
    addresses = ifaddresses.get(netifaces.AF_INET)
    if addresses is None:
        return None
    for address_set in addresses:
        brd = address_set['broadcast']
        if not brd.startswith('10.'):
            print('N/A')
            continue
        high, low = brd.split('.')[1:3]
        if high == '0':
            team_number = low
        else:
            team_number = high + low
        print(team_number)

if __name__ == "__main__":
    main()
