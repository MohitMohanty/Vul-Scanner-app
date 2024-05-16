#!/bin/bash
TARGET=$1
echo "Running Nmap scan on $TARGET..."
nmap -sV $TARGET -oN nmap_scan.txt

echo "Running WhoIs lookup on $TARGET..."
whois $TARGET > whois_scan.txt

echo "Running Dig lookup on $TARGET..."
dig $TARGET > dig_scan.txt
