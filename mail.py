import smtplib, ssl
from decouple import config

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.password = config("password")

    def send(self,sender_mail , emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()