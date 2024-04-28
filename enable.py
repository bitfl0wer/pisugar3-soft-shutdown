# Copyright (c) 2024 star
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import subprocess
import sys

services = ["pisugar3-check-shutdown", "pisugar3-set-shutdown"]

if os.geteuid() != 0:
    print("This script must be run as root (sudo). Exiting.")
    sys.exit()

for service in services:
    subprocess.run(["systemctl", "enable", "--now", service])
