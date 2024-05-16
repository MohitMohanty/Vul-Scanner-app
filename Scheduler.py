import schedule
import time
import subprocess

def job():
    target = input("Enter the target domain or IP: ")
    subprocess.call(['python3', 'Recon.py', target])
    subprocess.call(['python3', 'VulnScan.py', target])
    subprocess.call(['python3', 'ReportGenerator.py'])

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
