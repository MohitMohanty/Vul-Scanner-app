import subprocess

def run_vuln_scan(target):
    subprocess.call(['./VulnScan.sh', target])

def main():
    target = input("Enter the target URL: ")
    run_vuln_scan(target)

if __name__ == "__main__":
    main()
