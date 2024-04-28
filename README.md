# pisugar3-soft-shutdown

Soft shutdown functionality for the PiSugar 3 on Raspberry Pi devices via I2C over GPIO

## Versioning

Version 0.1.0

This repository uses [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## Dependencies

- `python3`, version 3.8 or later
- `i2c-tools python-smbus` installed on the Raspberry Pi (can be installed via apt)
- PiSugar 3 attached to the Raspberry Pi and in full working order

## Installation

1. Clone this repository to your Raspberry Pi
2. Run `sudo python3 install.py` to install and enable the necessary files and services.

Functionality can be disabled by running `sudo python3 disable.py` and re-enabled by
running `sudo python3 enable.py`.

## Uninstallation

1. Run `sudo python3 uninstall.py` to disable and remove all installed scripts and services.

## Usage

> [!IMPORTANT]
> Scripts need to be run as **root** using the `sudo` command.

When the power button on the PiSugar 3 is held for > 2 seconds, instead of killing the power to the
Raspberry Pi, the PiSugar 3 will set an I2C bit indicating that the Raspberry Pi should shut down.

This bit is read by the `check_shutdown.py` script, which will shut down the Raspberry Pi if the
bit is set. Before shutting down, the script will unset the bit to prevent the PiSugar 3 from
being unable to be powered down. If the bit were not unset, the PiSugar would continue to request
a shutdown instead of powering off.

When the Raspberry Pi is powered down, you can then use the
power button on the PiSugar 3 again to power down the UPS.

The systemd services provided by this repository will set the soft-shutdown bit on boot and continuously
check for the bit to be set, shutting down the Raspberry Pi if it is.
