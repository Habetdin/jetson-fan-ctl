#!/bin/sh

/usr/bin/jetson_clocks
echo 255 > /sys/devices/pwm-fan/target_pwm
sleep 10
