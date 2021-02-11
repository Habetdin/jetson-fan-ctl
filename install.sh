#!/bin/bash

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

mkdir -p /usr/local/bin/automagic-fan/
cp -R bin/. /usr/local/bin/automagic-fan/
chmod -R 0755 /usr/local/bin/automagic-fan/

mkdir /etc/automagic-fan/
cp cfg/config.json /etc/automagic-fan/
cp cfg/automagic-fan.path /lib/systemd/system/
cp cfg/automagic-fan.service /lib/systemd/system/
chmod 0644 /etc/automagic-fan/config.json
chmod 0644 /lib/systemd/system/automagic-fan.path
chmod 0644 /lib/systemd/system/automagic-fan.service

systemctl daemon-reload
systemctl enable automagic-fan.service
systemctl enable automagic-fan.path
systemctl start automagic-fan

echo "Automagic Fan Control have been installed!"
echo "To configure, edit /etc/automagic-fan/config.json (needs sudo)"
