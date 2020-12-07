import os
import smtplib

EMAIL_ADDRESS = 'testtesttesttest943@gmail.com'
EMAIL_PASSWORD = 'testtest@123'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

subject = 'Modified LogFiles Date'
body = 'Please check the modified dates of the below LogFiles and take the action if needed'

msg = f'Subject: {subject}\n\n{body}'

smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, 'testtesttesttest943@gmail.com', msg)


