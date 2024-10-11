#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

PAYLOAD_SIZE = 16
CHARACTER_DEVICE = "/dev/acer-gkbbl-0"

PAYLOAD_SIZE_STATIC_MODE = 4
CHARACTER_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-m',
                    type=int,
                    dest='mode',
                    default=3)

parser.add_argument('-z',
                    type=int,
                    dest='zone',
                    default=1)

parser.add_argument('-s',
                    type=int,
                    dest='speed',
                    default=4)

parser.add_argument('-b',
                    type=int,
                    dest='brightness',
                    default=100)

parser.add_argument('-d',
                    type=int,
                    dest='direction',
                    default=1)

parser.add_argument('-cR',
                    type=int,
                    dest='red',
                    default=50)

parser.add_argument('-cG',
                    type=int,
                    dest='green',
                    default=255)

parser.add_argument('-cB',
                    type=int,
                    dest='blue',
                    default=50)

args = parser.parse_args()


if args.mode == 0:
    # Static coloring mode
    payload = [0] * PAYLOAD_SIZE_STATIC_MODE
    if args.zone < 1 or args.zone > 8:
        print("Invalid Zone ID entered! Possible values are: 1, 2, 3, 4 from left to right")
    payload[0] = 1 << (args.zone - 1)
    payload[1] = args.red
    payload[2] = args.green
    payload[3] = args.blue
    with open(CHARACTER_DEVICE_STATIC, 'wb') as cd:
        cd.write(bytes(payload))

    # Tell WMI To use STATIC coloring
    # Dynamic coloring mode
    payload = [0] * PAYLOAD_SIZE
    payload[2] = args.brightness
    payload[9] = 1
    with open(CHARACTER_DEVICE, 'wb') as cd:
        cd.write(bytes(payload))

else:
    # Dynamic coloring mode
    payload = [0] * PAYLOAD_SIZE
    payload[0] = args.mode
    payload[1] = args.speed
    payload[2] = args.brightness
    payload[3] = 8 if args.mode == 3 else 0
    payload[4] = args.direction
    payload[5] = args.red
    payload[6] = args.green
    payload[7] = args.blue
    payload[9] = 1

    with open(CHARACTER_DEVICE, 'wb') as cd:
        cd.write(bytes(payload))
