import smtplib, ssl


class MailClient:
    """
    A class to simplify sending emails using Gmail's SMTP server.
    """

    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "aitmsams@gmail.com"
    receiver_email = "sum****ay9299@gmail.com"
    password = "huha **** **** wuac"  # Please replace with your password!
    subject = ""
    body = ""

    def __init__(self):
        """
        Creates a new MailClient object and creates a secure SSL context for sending emails.
        """
        self.context = ssl.create_default_context()

    def send(self):
        """
        Sends an email with the specified subject and body to the recipient email address.

        Raises:
            Exception: If there is an error while sending the email.
        """
        try:
            message = f"Subject: {self.subject}\n\n{self.body}"
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.ehlo()
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, self.receiver_email, message)
        except Exception as e:
            print(e)
