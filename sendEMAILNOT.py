import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# === 1. Konfigurasi Email ===
sender_email = "yourEmail@gmail.com"  # Ganti dengan email pengirim
password = "Google app password"  # Gunakan App Password dari Gmail

# === 2. Baca Daftar Penerima dari CSV ===
df = pd.read_csv("Untitled spreadsheet - Sheet1 (1).csv")

# === 3. Baca Template HTML untuk Penolakan ===
with open("email_rejection.html", "r", encoding="utf-8") as file:
    rejection_template = file.read()

# === 4. Kirim Email Penolakan ke Penerima yang Ditolak ===
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, password)

for index, row in df.iterrows():
    if row["DITERIMA"].strip().lower() == "tidak":  # Hanya mengirim ke yang ditolak
        receiver_email = row["EMAIL"]
        receiver_name = row["NAMA"]

        # Personalisasi email
        personalized_html = rejection_template.replace("{{NAMA}}", receiver_name)

        # Buat email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "Pemberitahuan Hasil Seleksi"
        msg.attach(MIMEText(personalized_html, "html"))

        # Kirim email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"❌ Email penolakan dikirim ke {receiver_name} ({receiver_email})")

# Tutup server
server.quit()
print("✅ Semua email penolakan berhasil dikirim!")