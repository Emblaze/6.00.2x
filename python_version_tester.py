#!/usr/bin/env python3
import platform
import struct
#import sys

print("Running Python version {} {}-bit on {} {}.".format(platform.python_version(), struct.calcsize("P" * 8), platform.system(), platform.machine()))
