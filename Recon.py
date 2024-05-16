import subprocess

def run_nmap_scan(target):
    subprocess.call(['./Recon.sh', target])

def main():
    target = input("Enter the target domain or IP: ")
    run_nmap_scan(target)

if __name__ == "__main__":
    main()
