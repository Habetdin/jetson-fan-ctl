# jetson-fan-control

Automagic Fan Control for the Nvidia Jetson Nano.

## Requirements:

Python 3 should be pre-installed on the Jetson Nano with standard system image.

You can check it using `python3 --version` command (3.5 or higher should be fine).

Otherwise, you can install it with `sudo apt install python3-dev`.

## How to install:

Run `sudo ./install.sh`. The Automagic Fan Control will automatically run at boot time.

It's a set-it-and-forget-it type thing, unless you want to mess with the fan speeds.

## How to customize:

Open /etc/automagic-fan/config.json with your favorite editor:

`sudo nano /etc/automagic-fan/config.json`

You will find the following lines:

```json
{
    "TEMPERATURE_MIN": 20,
    "TEMPERATURE_MAX": 50,
    "UPDATE_INTERVAL": 2
}
```

`TEMPERATURE_MIN` is the temperature (°C) below which the fan is turned off.

`TEMPERATURE_MAX` is the temperature (°C) above which the fan is running at 100% speed.

The script interpolates linearly between these two points.

`UPDATE_INTERVAL` is the time period between fan speed updates (in seconds).

You can use either integers (like 20) or floating point numbers (like 20.125) in each of these fields.

The temperature precision of the thermal sensors is 0.5 (°C), so don't expect this to be too precise.

Any changes in the script will be will be applied after the next reboot.

You can run `sudo systemctl restart automagic-fan` to apply changes immediately.

If you suspect something went wrong, please check `sudo systemctl status automagic-fan`.
