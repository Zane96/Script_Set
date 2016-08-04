#!/bin/bash

if test $# -gt 0; then
    case $1 in
        ao)
            ip="223.5.5.5 208.67.222.222"
            ;;
        ali)
            ip="223.5.5.5"
            ;;
        google)
            ip="8.8.8.8"
            ;;
        open)
            ip="208.67.222.222"
            ;;
        v2ex)
            ip="199.91.73.222"
            ;;
        dhcp)
            ip=Empty
            ;;
        *)
            ip=$1
    esac
    sudo networksetup -setdnsservers Wi-Fi $ip
else
    echo "Usage: dns [ao|ali|google|open|v2ex|dhcp|*]"
    echo "——"
fi

echo Current DNS: $(networksetup -getdnsservers Wi-Fi)