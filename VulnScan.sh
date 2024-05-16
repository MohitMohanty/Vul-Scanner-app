#!/bin/bash
TARGET=$1
echo "Running Nikto scan on $TARGET..."
nikto -h $TARGET -output nikto_scan.txt

echo "Running SQLMap scan on $TARGET..."
sqlmap -u $TARGET --batch --output-dir=sqlmap_scan

echo "Running WPScan on $TARGET..."
wpscan --url $TARGET --output wpscan_scan.txt

echo "Running SSLScan on $TARGET..."
sslscan $TARGET > sslscan_scan.txt
