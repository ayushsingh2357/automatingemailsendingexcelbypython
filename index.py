import os
import pandas as p
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
data = p.read_excel("mail list.xlsx")
email_col = data.get("email")
list_of_emails = list(email_col)
print(list_of_emails)
for emails in list_of_emails:

    try:
        server=sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(db_user, db_password)
        from_ = db_user
        to_ = emails
        # message['to'] = emails
        message=MIMEMultipart("GradsIT Academy")
        message['Subject'] = "Boost your college placement records by partnering with GradsIT Academy"
        message["from"] = db_user
        html = '''
                
        '''

        text = MIMEText(html, "html")
        message.attach(text)


        server.sendmail(from_, to_, message.as_string())
        # server.send_message(message)
    except Exception as e:
        print(e)
