#!/usr/bin/env python3
import struct
import sys

print("Running Python version: {} {}-bit on {}.".format(sys.version, struct.calcsize("P" * 8), sys.platform))
