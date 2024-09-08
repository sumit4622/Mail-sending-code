import smtplib, ssl


class MailClient:    
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "aitmsams@gmail.com"
    receiver_email = "sumit.ray9299@gmail.com"
    password = "huha dmqx lrkj wuac"
    subject = ""
    body = ""


    def __init__(self):
        self.context = ssl.create_default_context()


    def send(self):
        try:
            message = f"Subject: {self.subject}\n\n{self.body}"
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.ehlo()  
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, self.receiver_email, message)
        except Exception as e:
            print(e)