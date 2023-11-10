#!/bin/sh

fd ja3- utils/fingerprints/ -x yq -i 'del(.ip)' {}
fd ja3- utils/fingerprints/ -x yq -i 'del(.tcpip.ip.src_ip)' {}
