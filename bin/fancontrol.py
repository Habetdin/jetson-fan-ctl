#!/usr/bin/python3

import json
import time

THERMAL_SENSOR = '/sys/devices/virtual/thermal/thermal_zone0/temp'
FAN_TARGET_PWM = '/sys/devices/pwm-fan/target_pwm'

CONFIG_LOCATION = '/etc/automagic-fan/config.json'
TEMPERATURE_MIN = 20
TEMPERATURE_MAX = 42
UPDATE_INTERVAL = 3

try:
    print('Loading config from ' + CONFIG_LOCATION)
    with open(CONFIG_LOCATION, 'r') as f:
        config = json.load(f)
    if 'TEMPERATURE_MIN' in config:
        TEMPERATURE_MIN = float(config['TEMPERATURE_MIN'])
    if 'TEMPERATURE_MAX' in config:
        TEMPERATURE_MAX = float(config['TEMPERATURE_MAX'])
    if 'UPDATE_INTERVAL' in config:
        UPDATE_INTERVAL = float(config['UPDATE_INTERVAL'])
except:
    print('Error while loading configuration')
finally:
    print('Active configuration:')
    print('TEMPERATURE_MIN=' + str(TEMPERATURE_MIN))
    print('TEMPERATURE_MAX=' + str(TEMPERATURE_MAX))
    print('UPDATE_INTERVAL=' + str(UPDATE_INTERVAL))

time.sleep(max(10, UPDATE_INTERVAL))
with open(FAN_TARGET_PWM, 'w') as f:
   f.write('255')
time.sleep(max(10, UPDATE_INTERVAL))

while True:
    try:
        with open(THERMAL_SENSOR, 'r') as f:
            temp = float(f.read()) / 1000.0
        pwm = int(255 * (temp-TEMPERATURE_MIN) / (TEMPERATURE_MAX-TEMPERATURE_MIN))
        pwm = str(min(max(0, pwm), 255))
        with open(FAN_TARGET_PWM, 'w') as f:
            f.write(pwm)
        time.sleep(UPDATE_INTERVAL)
    except:
        pass
