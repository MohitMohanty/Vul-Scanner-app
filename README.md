Vulnerability Scanner Application
Overview
The Vulnerability Scanner Application is a comprehensive tool designed for red teamers to perform reconnaissance, vulnerability scanning, and report generation for target URLs. This application offers a user-friendly interface for initiating and managing scans efficiently.

How to Run
Clone the Repository:

bash
Copy code
git clone https://github.com/your_username/vulnerability-scanner.git
Navigate to the Directory:

bash
Copy code
cd vulnerability-scanner
Install Dependencies:

Copy code
pip install -r requirements.txt
Run the Application:

css
Copy code
python3 Main.py
Follow On-Screen Instructions:

Enter the target URL when prompted.
Choose from various options in the interactive menu:
Run Reconnaissance
Run Vulnerability Scan
Generate Report
Schedule Scans
Exit
Workflow
Start the Application:

Launch the application by running Main.py.
Input Target URL:

Enter the target URL when prompted. This input is used throughout the scanning process.
Select Options:

Choose from the main menu options to perform desired actions:
Run Reconnaissance
Run Vulnerability Scan
Generate Report
Schedule Scans
Exit
Scan Execution:

The application executes reconnaissance and vulnerability scanning tasks based on user selection.
Report Generation:

Generate a comprehensive PDF report containing all scan results for further analysis.
Schedule Scans (Optional):

Automate scan scheduling using the provided Scheduler.py script.
Exit:

Gracefully exit the application when finished.
Contributors
Mohit Mohanty (GitHub)
