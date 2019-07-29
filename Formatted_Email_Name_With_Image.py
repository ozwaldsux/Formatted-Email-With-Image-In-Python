import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

host = "smtp.gmail.com"
port = 587
username = "youremail@gmail.com"
password = "password"
from_email = "youremail@gmail.com"
to_list = [""]

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """\
<html>
  <head></head>
  <body>
    <p>Hi <br><br>

<img src="cid:image1">
<br><br>

    </p>
  </body>
</html>
"""

        
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name [1:].lower()
        amount = "%.2f" %(amount)
        detail = { 
        "name": name,
        "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                    )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return[]
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Subject"
                    the_msg["From"] = str('Your Name <youremail@gmail.com>')
                    the_msg['To'] = user_email 
                    part_1 = MIMEText(user_message, 'html')
                    the_msg.attach(part_1)
                    # This example assumes the image is in the current directory
                    fp = open('Path/to/your/photo.png', 'rb')
                    msgImage = MIMEImage(fp.read())
                    fp.close()
                    # Define the image's ID as referenced above
                    msgImage.add_header('Content-ID', '<image1>')
                    the_msg.attach(msgImage)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("error sending message")
            return True
        return False

    

obj = MessageUser()




obj.get_details()

obj.send_email()

