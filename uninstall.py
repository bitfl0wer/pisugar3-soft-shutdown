# Copyright (c) 2024 star
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import subprocess
import sys

dest_directory = "/usr/local/share/pisugar3-soft-shutdown"
files_to_remove = ["check-soft-shutdown.py", "set-soft-shutdown.py"]

systemd_dest_directory = "/etc/systemd/system"
systemd_files_to_remove = [
    "pisugar3-check-shutdown.service",
    "pisugar3-set-shutdown.service",
]

if os.geteuid() != 0:
    print("This script must be run as root (sudo). Exiting.")
    sys.exit()

# disable systemd services
subprocess.run(["python3", "./disable.py"])

for file in files_to_remove:
    os.remove(os.path.join(dest_directory, file))

for file in systemd_files_to_remove:
    os.remove(os.path.join(systemd_dest_directory, file))

# if dest_directory is empty, remove it
if not os.listdir(dest_directory):
    os.rmdir(dest_directory)

subprocess.run(["systemctl", "daemon-reload"])
