from mail import Mail

if __name__ == "__main__":
    mails = ["RECEIVER MAIL"]
    send_mail = "SENDER MAIL"
    subject = "SUBJECT"
    content = "CONTENT"

    mail = Mail()
    mail.send(send_mail,mails, subject, content)