#!/bin/bash

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

systemctl stop automagic-fan

rm -rf /usr/local/bin/automagic-fan/
rm -rf /etc/automagic-fan/
rm /lib/systemd/system/automagic-fan.path
rm /lib/systemd/system/automagic-fan.service

systemctl daemon-reload

echo "Automagic Fan Control have been uninstalled!"
