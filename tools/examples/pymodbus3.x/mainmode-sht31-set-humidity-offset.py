#!/usr/bin/python

"""
/*********************************************************************
 * Software License Agreement (BSD License)
 *
 * Copyright (c) 2018, 2023
 *
 * Balint Cristian <cristian dot balint at gmail dot com>
 * Stefan Reichhard <s.reichhard@netMedia.pro>
 *
 * TinnyModbus
 *
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *
 *   * Neither the name of the copyright holders nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *
 *********************************************************************/
"""

"""

  mainmode-set-Humidity-offset.py (calibrate Humidity Value)

"""

import sys
import logging

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client import ModbusSerialClient as ModbusClient



logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# create connection (main mode is 38400)
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=38400, timeout=1.5)
client.connect()

try:
  slvaddr = int(sys.argv[1])
  offset = int(sys.argv[2])
except:
  print ("usage: %s [slvaddr] [humidity offset]" % sys.argv[0])
  print ("[humidity offset] : 0 to 127 represents 0.0 to +12.7 %RH and 255 to 128: -0.1 to -12.8 %RH offset (8 bit signed int)")
  sys.exit(-1)

print ("modbus cmd: 0x06 addr: 0x0021 value: 0x%04x length: 0x01\n" % offset)
result  = client.write_register(address=0x0021, value=offset, count=0x01, slave=slvaddr)
print (result)

print ("")

client.close()
