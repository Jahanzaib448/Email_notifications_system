# Multi Email Notifier — Styled (Python + Tkinter)

A modern, beautifully designed Tkinter GUI application that allows you to send a single email to multiple recipients using SMTP. It supports Gmail App Password authentication, includes a gradient user interface, and prevents freezing using background threading.

---

## 📌 Project Overview

This project is a **Styled Multi Email Sender GUI** built with Python (Tkinter).  
It allows you to:

- Send the same email to multiple recipients  
- Use Gmail SMTP (supports App Password)  
- Enjoy a modern gradient Purple-Pink UI  
- Avoid GUI freezing (thanks to threading)  
- View real-time logs showing success and failures  

---

## ✨ Features

- Send email to multiple users at once  
- Beautiful gradient theming  
- Background threading (non-blocking GUI)  
- Email validation using regex  
- Supports SSL (465) and TLS (587)  
- Hover-styled buttons  
- Scrollable log window  
- Separate fields for SMTP server and port  

---

## 🧩 Requirements

No external libraries required.  
Only Python’s built-in modules:

- Python 3.8+
- tkinter
- smtplib
- email.message
- threading
- re

---

## 📁 File Structure

```
|-- multi_email_notifier_styled.py
|-- README.md
```

---

## 🔧 Installation

1. Install Python (if not installed).
2. Download or clone this project.
3. Run the script:

```bash
python multi_email_notifier_styled.py
```

---

## ⚙️ Gmail Configuration (Important)

Gmail requires an **App Password**.  
Normal Gmail password will **NOT** work.

### 🔑 Generate Gmail App Password:

1. Go to **Google Account → Security**
2. Enable **2-Step Verification**
3. Go to **App Passwords**
4. Choose:
   - App: *Mail*
   - Device: *Windows Computer* (or any)
5. Google will generate a **16-digit password**
6. Enter it inside the app

### Default SMTP Settings:

```
SMTP Server: smtp.gmail.com
Port (SSL): 465
Port (TLS): 587
```

---

## ▶️ How to Use

### 1️⃣ Launch the program
```bash
python multi_email_notifier_styled.py
```

### 2️⃣ Enter:
- Sender Email  
- App Password  
- SMTP Server  
- Port  

### 3️⃣ Add multiple recipients
Use comma or newlines:

```
one@gmail.com
two@yahoo.com, three@hotmail.com
```

### 4️⃣ Enter Subject & Message Body

### 5️⃣ Click **Send Emails**

You will see delivery logs in the status window.

---

## 🧪 Email Validation

The app checks:

- Invalid email formats  
- Missing recipients  
- Missing sender credentials  
- Confirmation popup before sending  

---

## 📬 Sample Log Output

```
Preparing to send to 3 recipients...
Connecting to SMTP server smtp.gmail.com:465...
Logged in. Starting sending...
[1/3] Sent to abc@gmail.com
[2/3] FAILED xyz@yahoo.com — SMTPAuthenticationError
[3/3] Sent to def@hotmail.com

Done. Sent 2/3 messages.
--- Operation finished ---
```

---

## 🛠 Troubleshooting

### ❌ Authentication Error
Use **App Password**, not your normal Gmail password.

### ❌ Port Error
Try:
- **465** (SSL)
- **587** (TLS)

### ❌ Email Not Sending
- Check your internet
- Check App Password
- Check email formatting

---

## 🤝 Contributing

Suggestions and feature requests are welcome!

Possible future upgrades:
- Dark mode  
- Add email
