#!/usr/bin/env python3
"""
multi_email_notifier_styled.py
Styled Tkinter GUI to send one email to multiple recipients using SMTP (Gmail example).
Run: python multi_email_notifier_styled.py
"""

import re
import threading
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font

# -------------------------
# Helper functions
# -------------------------
def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email.strip()) is not None

# -------------------------
# Email sending logic
# -------------------------
def send_emails_thread(sender_email, sender_pass, smtp_server, smtp_port,
                       recipients_list, subject, body, gui_callback):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["Subject"] = subject
    msg.set_content(body)

    total = len(recipients_list)
    sent_count = 0

    try:
        gui_callback(f"Connecting to SMTP server {smtp_server}:{smtp_port}...\n", False)
        if smtp_port == 465:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=20)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port, timeout=20)
            server.ehlo()
            try:
                server.starttls()
                server.ehlo()
            except Exception:
                pass

        server.login(sender_email, sender_pass)
        gui_callback("Logged in. Starting sending...\n", False)

        for i, rcpt in enumerate(recipients_list, 1):
            rcpt = rcpt.strip()
            if not rcpt:
                continue
# Create a fresh message for each recipient
            new_msg = EmailMessage()
            new_msg["From"] = sender_email
            new_msg["To"] = rcpt
            new_msg["Subject"] = subject
            new_msg.set_content(body)

            try:
                server.send_message(new_msg)

                sent_count += 1
                gui_callback(f"[{i}/{total}] Sent to {rcpt}\n", False)
            except Exception as e:
                gui_callback(f"[{i}/{total}] FAILED {rcpt} — {e}\n", False)

        server.quit()
        gui_callback(f"\nDone. Sent {sent_count}/{total} messages.\n", True)
    except Exception as e:
        gui_callback(f"\nERROR: {e}\n", True)


# -------------------------
# Styled GUI
# -------------------------
class MultiEmailNotifier(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi Email Notifier — Styled")
        self.geometry("820x620")
        self.resizable(False, False)

        # Theme colors (Purple + Pink Gradient)
        self._c1 = "#2b0b3a"   # deep purple (top)
        self._c2 = "#6a148f"   # purple
        self._c3 = "#d76bdc"   # pink

        # Create gradient background on a Canvas
        self.canvas = tk.Canvas(self, width=820, height=620, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self._draw_gradient(self.canvas, self._c1, self._c2, self._c3)

        # Create a translucent-ish panel to host controls
        main_panel = tk.Frame(self.canvas, bg="#ffffff", bd=0, highlightthickness=0)
        main_panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=780, height=560)

        # Drop shadow effect (simple)
        shadow = tk.Frame(self.canvas, bg="#b49ac5", bd=0)
        shadow.place(x=25, y=25, width=784, height=564)
        main_panel.lift()  # bring panel above shadow

        # Fonts
        self.header_font = font.Font(family="Segoe UI", size=14, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=10)
        self.input_font = font.Font(family="Segoe UI", size=10)
        self.btn_font = font.Font(family="Segoe UI", size=10, weight="bold")
        self.small_font = font.Font(family="Segoe UI", size=9)

        # Use ttk styles for entries and frames
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Card.TLabelframe", background="#ffffff", borderwidth=0)
        style.configure("TLabel", background="#ffffff", font=self.label_font)
        style.configure("TEntry", font=self.input_font)
        style.configure("TButton", font=self.btn_font, padding=6)

        # Top frame for account settings
        account_frame = ttk.LabelFrame(main_panel, text=" SMTP Account & Server ", style="Card.TLabelframe")
        account_frame.place(x=12, y=12, width=756, height=120)

        ttk.Label(account_frame, text="Sender Email:").place(x=12, y=12)
        self.entry_sender = ttk.Entry(account_frame, width=36)
        self.entry_sender.place(x=120, y=12)

        ttk.Label(account_frame, text="App Password:").place(x=12, y=44)
        self.entry_password = ttk.Entry(account_frame, show="*", width=36)
        self.entry_password.place(x=120, y=44)

        ttk.Label(account_frame, text="SMTP Server:").place(x=460, y=12)
        self.entry_smtp = ttk.Entry(account_frame, width=22)
        self.entry_smtp.place(x=550, y=12)
        self.entry_smtp.insert(0, "smtp.gmail.com")

        ttk.Label(account_frame, text="Port:").place(x=460, y=44)
        self.entry_port = ttk.Entry(account_frame, width=8)
        self.entry_port.place(x=550, y=44)
        self.entry_port.insert(0, "465")

        ttk.Label(account_frame, text="Tip: Use App Password for Gmail.", foreground="#666666", font=self.small_font).place(x=12, y=78)

        # Recipients frame (left)
        recipients_frame = ttk.LabelFrame(main_panel, text=" Recipients (comma or newline) ", style="Card.TLabelframe")
        recipients_frame.place(x=12, y=144, width=380, height=256)

        self.txt_recipients = scrolledtext.ScrolledText(recipients_frame, wrap=tk.WORD, width=42, height=12, font=self.input_font)
        self.txt_recipients.pack(expand=True, fill=tk.BOTH, padx=6, pady=6)

        # Message frame (right)
        message_frame = ttk.LabelFrame(main_panel, text=" Message ", style="Card.TLabelframe")
        message_frame.place(x=404, y=144, width=364, height=320)

        ttk.Label(message_frame, text="Subject:").place(x=8, y=8)
        self.entry_subject = ttk.Entry(message_frame, width=44)
        self.entry_subject.place(x=8, y=28)

        ttk.Label(message_frame, text="Body:").place(x=8, y=56)
        self.txt_body = scrolledtext.ScrolledText(message_frame, wrap=tk.WORD, width=44, height=14, font=self.input_font)
        self.txt_body.place(x=8, y=76)

        # Buttons area
        # Colored Send button (pink gradient style)
        self.send_btn = tk.Button(main_panel, text="Send Emails", font=self.btn_font,
                                  bd=0, relief=tk.FLAT, activebackground="#c74fbf",
                                  command=self.on_send)
        self.send_btn.place(x=12, y=410, width=380, height=44)
        self._style_button(self.send_btn, bg="#e85cf6", fg="white")

        # Clear Log button (outline style)
        self.clear_btn = tk.Button(main_panel, text="Clear Log", font=self.btn_font,
                                   bd=1, relief=tk.RIDGE, command=self.clear_log)
        self.clear_btn.place(x=404, y=410, width=120, height=36)
        self._style_button(self.clear_btn, bg="#ffffff", fg="#6a148f", border=True)

        # Status area (with subtle rounded border look)
        status_holder = tk.Frame(main_panel, bg="#faf7ff", bd=1, relief=tk.SOLID)
        status_holder.place(x=12, y=462, width=756, height=86)
        self.status_area = scrolledtext.ScrolledText(status_holder, wrap=tk.WORD, width=88, height=4, font=self.small_font)
        self.status_area.place(x=4, y=4, width=748, height=78)
        self.status_area.configure(state=tk.DISABLED)

        # Footer
        footer = tk.Label(main_panel, text="Made with ❤️  — Paste multiple emails, set subject & message, then press Send.",
                          bg="#ffffff", fg="#7a6b8f", font=self.small_font)
        footer.place(x=12, y=556)

    # Gradient drawing helper (vertical gradients)
    def _draw_gradient(self, canvas, c1, c2, c3):
        # draw top-to-bottom gradient in two steps
        w = 820
        h = 620
        steps = max(h // 2, 1)
        for i in range(steps):
            r1, g1, b1 = self._hex_to_rgb(c1)
            r2, g2, b2 = self._hex_to_rgb(c2)
            t = i / steps
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_rectangle(0, int(i * (h / steps)), w, int((i + 1) * (h / steps)), outline=color, fill=color)
        # second gradient section
        steps2 = max(h // 2, 1)
        for i in range(steps2):
            r1, g1, b1 = self._hex_to_rgb(c2)
            r2, g2, b2 = self._hex_to_rgb(c3)
            t = i / steps2
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
            color = f"#{r:02x}{g:02x}{b:02x}"
            y1 = int(h / 2 + i * (h / (2 * steps2)))
            y2 = int(h / 2 + (i + 1) * (h / (2 * steps2)))
            canvas.create_rectangle(0, y1, w, y2, outline=color, fill=color)

    def _hex_to_rgb(self, h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    def _style_button(self, btn, bg="#e85cf6", fg="white", border=False):
        # simple custom style for a tk.Button (not ttk) with hover
        btn.configure(bg=bg, fg=fg, activeforeground=fg, activebackground=bg, highlightthickness=0)
        if border:
            btn.configure(relief=tk.RIDGE, bd=1)
        # store original color
        btn._orig_bg = bg
        # hover effect
        def on_enter(e):
            btn.configure(bg=self._darker_color(btn._orig_bg, 0.9))
        def on_leave(e):
            btn.configure(bg=btn._orig_bg)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def _darker_color(self, hexcol, factor=0.9):
        r, g, b = self._hex_to_rgb(hexcol)
        r = max(0, int(r * factor))
        g = max(0, int(g * factor))
        b = max(0, int(b * factor))
        return f"#{r:02x}{g:02x}{b:02x}"

    def append_status(self, txt: str, done: bool):
        self.status_area.configure(state=tk.NORMAL)
        self.status_area.insert(tk.END, txt)
        self.status_area.see(tk.END)
        if done:
            self.status_area.insert(tk.END, "\n--- Operation finished ---\n")
        self.status_area.configure(state=tk.DISABLED)

    def clear_log(self):
        self.status_area.configure(state=tk.NORMAL)
        self.status_area.delete("1.0", tk.END)
        self.status_area.configure(state=tk.DISABLED)

    def on_send(self):
        sender = self.entry_sender.get().strip()
        password = self.entry_password.get().strip()
        smtp_server = self.entry_smtp.get().strip() or "smtp.gmail.com"
        try:
            port = int(self.entry_port.get().strip())
        except Exception:
            messagebox.showerror("Invalid Port", "SMTP port must be a number (e.g., 465 or 587).")
            return

        raw_recipients = self.txt_recipients.get("1.0", tk.END).strip()
        recipients = []
        for part in re.split(r"[,\n]+", raw_recipients):
            if part.strip():
                recipients.append(part.strip())

        subject = self.entry_subject.get().strip() or "(No Subject)"
        body = self.txt_body.get("1.0", tk.END).strip() or ""

        if not sender:
            messagebox.showerror("Missing Sender", "Please enter sender email.")
            return
        if not password:
            messagebox.showerror("Missing Password", "Please enter app password.")
            return
        if not recipients:
            messagebox.showerror("No Recipients", "Please enter at least one recipient email.")
            return

        invalid = [r for r in recipients if not is_valid_email(r)]
        if invalid:
            messagebox.showerror("Invalid Emails", f"The following emails look invalid:\n{', '.join(invalid)}")
            return

        confirm = messagebox.askyesno("Confirm", f"Send this email to {len(recipients)} recipients?\nSubject: {subject}")
        if not confirm:
            return

        for w in self.winfo_children():
            if isinstance(w, tk.Button):
                w.configure(state=tk.DISABLED)

        def gui_callback(text, done):
            self.after(1, lambda: self.append_status(text, done))
            if done:
                def reenable():
                    for w in self.winfo_children():
                        if isinstance(w, tk.Button):
                            w.configure(state=tk.NORMAL)
                self.after(1, reenable)

        self.append_status(f"Preparing to send to {len(recipients)} recipients...\n", False)

        thread = threading.Thread(
            target=send_emails_thread,
            args=(sender, password, smtp_server, port, recipients, subject, body, gui_callback),
            daemon=True
        )
        thread.start()


if __name__ == "__main__":
    app = MultiEmailNotifier()
    app.mainloop()
