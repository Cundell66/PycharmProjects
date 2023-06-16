import smtplib
from email.message import EmailMessage

email_content = """
Dear Paul,

This is an email sent by Python.

    Bloody good innit?
    
Cheers
        Paul
"""


email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'coding@stonefallworld.com'
email['To'] = 'paul@stonefallworld.com'

email.set_content(email_content)


smtp_connector = smtplib.SMTP(host='mail.stonefallworld.com', port=587)
smtp_connector.starttls()
smtp_connector.login('coding@stonefallworld.com', 'THom@$93')

smtp_connector.send_message(email)
smtp_connector.quit()
