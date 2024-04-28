# Copyright (c) 2024 bitfl0wer
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import time

import smbus

bus = smbus.SMBus(1)
device_address = 0x57

while True:
    register_address = 0x03
    data = bus.read_byte_data(device_address, register_address)

    # Check if the 3rd bit is set
    if data & (1 << 3):
        data &= ~(1 << 4)
        bus.write_byte_data(device_address, register_address, data)

        # Initiate a system shutdown
        os.system("sudo shutdown -h now")
        break

    # Sleep for a bit to avoid a busy loop
    time.sleep(1)
