# Multi Email Notifier — Styled (Python + Tkinter)

یہ README فائل آپ کے **multi_email_notifier_styled.py** پروجیکٹ کی مکمل وضاحت دیتی ہے۔ یہ ایک خوبصورت GUI ایپ ہے جو ایک ہی ای میل مختلف لوگوں کو ایک ساتھ بھیجنے کے لیے استعمال ہوتی ہے۔

---

## 📌 پروجیکٹ کا تعارف

یہ Python Tkinter کی مدد سے بنایا گیا ایک **Styled Multi Email Sender GUI** ہے جو:

* ایک ہی ای میل کئی ریسیورز کو بھیجتا ہے
* Gmail SMTP (App Password) کو سپورٹ کرتا ہے
* خوبصورت گرادیئنٹ GUI رکھتا ہے
* بیک گراؤنڈ میں تھریڈنگ استعمال کر کے ایپ کو فریز ہونے سے بچاتا ہے
* لاگ اسٹیٹس دکھاتا ہے کہ کون سی میل کامیاب/فیل ہوئی

---

## ✨ خصوصیات (Features)

* متعدد ای میلز ایک ساتھ بھیجنے کی سہولت
* سکریپٹ فریز نہ ہو — بیک گراؤنڈ تھریڈ
* گرادیئنٹ اسٹائلڈ GUI (Purple + Pink Theme)
* Valid Email Check (Regex Based)
* SMTP SSL / TLS Support (465 / 587)
* Send Log Window
* Buttons with Hover Effects

---

## 🧩 ضروریات (Requirements)

اس پروجیکٹ کو چلانے کے لیے درج ذیل چیزیں درکار ہوں گی:

* Python 3.8 یا جدید
* Built‑in libraries:

  * tkinter
  * smtplib
  * email
  * threading
  * re

کسی ایکسٹرا لائبریری کی ضرورت نہیں۔

---

## 📁 فائل اسٹرکچر

```
|-- multi_email_notifier_styled.py
|-- README.md (This file)
```

---

## 🔧 انسٹالیشن

1. Python انسٹال کریں (اگر پہلے سے نہیں)
2. اس فائل کو ڈاؤنلوڈ کریں یا اپنے فولڈر میں کاپی کریں:

   ```bash
   multi_email_notifier_styled.py
   ```
3. کوڈ رن کریں:

   ```bash
   python multi_email_notifier_styled.py
   ```

---

## ⚙️ کنفیگریشن

آپ کو Gmail App Password استعمال کرنا ہوگا۔

### 🔑 Gmail App Password کیسے لیں؟

1. Google Account → Security → App Passwords
2. “Mail” → “Windows Computer” سلیکٹ کریں
3. 16‑digit password کو یہاں استعمال کریں:

   * **Sender Email**
   * **App Password**

SMTP Settings:

```
SMTP Server: smtp.gmail.com
Port: 465 (SSL) OR 587 (TLS)
```

---

## ▶️ استعمال کا طریقہ (How to Use)

### 1️⃣ ایپ اوپن کریں

```bash
python multi_email_notifier_styled.py
```

### 2️⃣ Sender Email & App Password دیں

### 3️⃣ SMTP Server & Port سیٹ کریں (Default already set):

* smtp.gmail.com
* port 465

### 4️⃣ Recipients ڈالیں

* comma سے الگ کریں، یا
* نئی لائن استعمال کریں

```
one@gmail.com
two@gmail.com, three@yahoo.com
```

### 5️⃣ Subject اور Body لکھیں

### 6️⃣ “Send Emails” دبائیں

اپریشن اسٹیٹس نیچے والی Log Window میں نظر آئے گا۔

---

## 🧪 Email Validation

کوڈ خود چیک کرتا ہے کہ:

* غلط ای میل فارمیٹ ہو تو **Error** آئے
* خالی recipient لسٹ ہو تو **Error** آئے
* Confirmation Box آئے گا: “Send to X recipients?”

---

## 🧵 Threading

ایپ فریز نہ ہو، اس کے لیے ای میل بھیجنے کا عمل **background thread** میں چلتا ہے۔

---

## 📬 Output Log Example

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

* App Password ضرور استعمال کریں — Normal Gmail Password نہیں چلتا۔

### ❌ Less Secure App Error

* Gmail اب direct password login allow نہیں کرتا — App Password ضروری ہے۔

### ❌ Port Error

* 465 (SSL) try کریں
* یا 587 (TLS)

---

## 🤝 Contributing

اگر آپ اس میں مزید فیچرز شامل کروانا چاہتے ہیں:

* Dark Mode
* Export Log Button
* Import Email CSV
* Attachments Support
  مجھے بتائیں — میں آپ کے لیے شامل کر دوں گا۔

---

## © License

Free to use. No restrictions.
