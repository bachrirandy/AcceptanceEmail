import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# === 1. Konfigurasi Email ===
sender_email = "yourEmail@gmail.com"  # Ganti dengan email pengirim
password = "Password"  # Gunakan App Password dari Gmail

# === 2. Baca Daftar Penerima dari CSV ===
df = pd.read_csv("Untitled spreadsheet - Sheet1 (1).csv")

# === 3. Baca Template HTML ===
with open("email.html", "r", encoding="utf-8") as file:
    acceptance_template = file.read()

with open("email_rejection.html", "r", encoding="utf-8") as file:
    rejection_template = file.read()

# === 4. Kirim Email Berdasarkan Status Penerimaan ===
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, password)

for index, row in df.iterrows():
    # Cek apakah nilai email valid
    receiver_email = row["EMAIL"]
    if isinstance(receiver_email, str):
        receiver_email = receiver_email.strip()
    else:
        print(f"❌ Invalid email at row {index + 1}. Skipping.")
        continue

    receiver_name = row["NAMA"].strip() if isinstance(row["NAMA"], str) else ""
    status = row["DITERIMA"].strip().lower() if isinstance(row["DITERIMA"], str) else ""
    dinas = row["DINAS"].strip() if isinstance(row["DINAS"], str) else ""
    
    if status == "ya":
        email_template = acceptance_template.replace("{{NAMA}}", receiver_name).replace("{{DINAS}}", dinas)
        subject = "Selamat! Anda Diterima"
    else:
        email_template = rejection_template.replace("{{NAMA}}", receiver_name)
        subject = "Pemberitahuan Hasil Seleksi"
    
    # Buat email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(email_template, "html"))
    
    # Kirim email
    try:
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"✅ Email berhasil dikirim ke {receiver_name} ({receiver_email}) dengan status {status.upper()}")
    except Exception as e:
        print(f"❌ Gagal mengirim email ke {receiver_email}. Error: {e}")

# Tutup server
server.quit()
print("✅ Semua email berhasil dikirim!")
