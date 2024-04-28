# Copyright (c) 2024 star
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import shutil
import subprocess
import sys

src_directory = "./tasks"
dest_directory = "/usr/local/share/pisugar3-soft-shutdown"
files_to_copy = ["check-soft-shutdown.py", "set-soft-shutdown.py"]

systemd_src_directory = "./systemd"
systemd_dest_directory = "/etc/systemd/system"
systemd_files_to_copy = [
    "pisugar3-check-shutdown.service",
    "pisugar3-set-shutdown.service",
]

if os.geteuid() != 0:
    print("This script must be run as root (sudo). Exiting.")
    sys.exit()

if not os.path.exists(dest_directory):
    os.makedirs(dest_directory)

for file in files_to_copy:
    shutil.copy2(os.path.join(src_directory, file), dest_directory)

for file in systemd_files_to_copy:
    shutil.copy2(os.path.join(systemd_src_directory, file), systemd_dest_directory)

subprocess.run(["systemctl", "daemon-reload"])

subprocess.run(["python3", "./enable.py"])
