import subprocess

def main_menu():
    print("Vulnerability Scanner")
    print("1. Run Reconnaissance")
    print("2. Run Vulnerability Scan")
    print("3. Generate Report")
    print("4. Schedule Scans")
    print("5. Exit")
    choice = input("Select an option: ")
    return choice

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            target = input("Enter the target domain or IP: ")
            subprocess.call(['python3', 'Recon.py', target])
        elif choice == '2':
            target = input("Enter the target URL: ")
            subprocess.call(['python3', 'VulnScan.py', target])
        elif choice == '3':
            subprocess.call(['python3', 'ReportGenerator.py'])
            print("Report generated as Vulnerability_Report.pdf")
        elif choice == '4':
            print("Scheduling Scans...")
            subprocess.call(['python3', 'Scheduler.py'])
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()