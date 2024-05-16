from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report():
    # Create a SimpleDocTemplate object with specified page size
    doc = SimpleDocTemplate("Vulnerability_Report.pdf", pagesize=A4)

    # Create a list to hold the report content
    report_content = []

    # Add Nmap Results
    with open('nmap_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("Nmap Scan Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Add WhoIs Results
    with open('whois_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("WhoIs Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Add Dig Results
    with open('dig_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("Dig Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Add Nikto Results
    with open('nikto_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("Nikto Scan Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Add SQLMap Results
    sqlmap_scan_dir = 'sqlmap_scan'
    if os.path.exists(sqlmap_scan_dir) and os.path.isdir(sqlmap_scan_dir):
        sqlmap_scan_file = os.path.join(sqlmap_scan_dir, 'log')
        if os.path.exists(sqlmap_scan_file):
            with open(sqlmap_scan_file, 'r') as file:
                content = file.read()
                report_content.append(Paragraph("SQLMap Scan Results:", getSampleStyleSheet()["Heading1"]))
                report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))
        else:
            report_content.append(Paragraph("No SQLMap scan results found.", getSampleStyleSheet()["Heading1"]))
    else:
        report_content.append(Paragraph("SQLMap scan directory not found.", getSampleStyleSheet()["Heading1"]))

    # Add WPScan Results
    with open('wpscan_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("WPScan Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Add SSLScan Results
    with open('sslscan_scan.txt', 'r') as file:
        content = file.read()
        report_content.append(Paragraph("SSLScan Results:", getSampleStyleSheet()["Heading1"]))
        report_content.append(Paragraph(content.replace('\n', '<br/>'), getSampleStyleSheet()["Normal"]))

    # Build the PDF document
    doc.build(report_content)

if __name__ == "__main__":
    generate_report()
