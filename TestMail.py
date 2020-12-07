import os
import smtplib
import time

EMAIL_ADDRESS = 'testtesttesttest943@gmail.com'
EMAIL_PASSWORD = 'testtest@123'

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

Part1 = "Please check the modified dates of the below LogFiles and take the action if needed. \n \n"
Part2 = "File Name: %s \n" % os.path.basename("C:/users/admin/Desktop/New Text Document.txt")
Part3 = "Last Modified: %s" % time.ctime(os.path.getmtime("C:/users/admin/Desktop/New Text Document.txt"))

subject = 'Modified LogFiles Date'
body = Part1 + Part2 + Part3

msg = f'Subject: {subject}\n\n{body}'

server.sendmail("testtesttesttest943@gmail.com",
                "testtesttesttest943@gmail.com",
                msg)

server.quit()

#'Please check the modified dates of the below LogFiles and take the action if needed'
