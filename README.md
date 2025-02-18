# Email Sender with Python (SMTP & Pandas)

This project is a Python script that automatically sends emails based on data retrieved from a CSV file. It uses Gmail's SMTP server, Pandas for data processing, and MIME for email formatting.

## 📌 Features

- Reads recipient list from a CSV file.
- Customizes email content based on acceptance status.
- Uses HTML templates for emails.
- Automatically sends emails via Gmail SMTP.
- Displays email delivery status.

## 📂 File Structure

|-- email_sender.py # Main script for sending emails 
|-- email.html # Email template for accepted recipients 
|-- email_rejection.html # Email template for rejected recipients 
|-- recipients.csv # CSV file containing recipient details 
|-- README.md # Project documentation


## 🔧 Setup

### 1. Generate an App Password in Gmail

Since Gmail does not allow direct login with your account password, you need to use an App Password. Follow these steps:

1. Log into your Google account.
2. Navigate to **Security** > **App Passwords**.
3. Create an **App Password** for Mail.
4. Save the generated password for use in the script.

### 2. Install Dependencies

Ensure that the required libraries are installed by running the following command:

```bash
pip install pandas smtplib email.mime
```

### 3. Prepare the CSV File

## 🚀 How to Run

1. Edit email_sender.py and replace sender_email with your Gmail address.
2. Replace password with your Gmail App Password.
3. Run the script using the following command:

```bash
python email_sender.py
```

## 📝 Important Notes
1. Ensure that the sender email is enabled for Less Secure Apps or uses an App Password.
2. Avoid storing passwords directly in the code. Use .env files or environment variables for better security.
3. Gmail has a daily sending limit. If exceeded, consider using another email service or limiting the number of emails sent.



