# Copyright (c) 2024 bitfl0wer
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import smbus

bus = smbus.SMBus(1)
device_address = 0x57

register_address = 0x03
data = bus.read_byte_data(device_address, register_address)

# Turn on the 4th bit to activate the soft shutdown function
data |= 1 << 4

bus.write_byte_data(device_address, register_address, data)
