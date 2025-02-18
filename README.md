Email Sender with Python (SMTP & Pandas)

This project is a Python script for automatically sending emails based on data retrieved from a CSV file. The script utilizes Gmail SMTP, Pandas for data processing, and MIME for email formatting.

📌 Features

Reads recipient list from a CSV file

Customizes email content based on acceptance status

Uses HTML templates for emails

Automatically sends emails via Gmail SMTP

Displays email delivery status

📂 File Structure

|-- email_sender.py  # Main script for sending emails
|-- email.html       # Email template for accepted recipients
|-- email_rejection.html  # Email template for rejected recipients
|-- recipients.csv   # CSV file containing recipient details
|-- README.md        # Project documentation

🔧 Setup

1. Generate an App Password in Gmail

Since Gmail does not allow direct login with an account password, use an App Password by following these steps:

Log into your Google account.

Navigate to Security > App Passwords.

Create an App Password for Mail.

Save the generated password for use in the script.

2. Install Dependencies

Ensure that the required libraries are installed by running the following command:

pip install pandas smtplib email.mime

3. Prepare the CSV File

Create a recipients.csv file with the following format:

EMAIL,NAMA,DITERIMA,DINAS
email1@example.com,Name1,yes,Division A
email2@example.com,Name2,no,
email3@example.com,Name3,yes,Division B

EMAIL: Recipient's email address

NAMA: Recipient's name

DITERIMA: yes if accepted, no if rejected

DINAS: Division or department (only applicable if accepted)

🚀 How to Run

Edit email_sender.py and replace sender_email with your Gmail address.

Replace password with your Gmail App Password.

Run the script using the following command:

python email_sender.py

Emails will be sent based on the data in recipients.csv.

📝 Important Notes

Ensure that the sender email is enabled for Less Secure Apps or uses an App Password.

Avoid storing passwords directly in the code. Use .env files or environment variables for better security.

Gmail has a daily sending limit. If exceeded, consider using another email service or limiting the number of emails sent.

📜 License

This project is intended for educational and personal use. Please use it responsibly and refrain from misuse such as spam or phishing.
