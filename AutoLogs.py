import os
import os.path, time
import smtplib


def ModifiedDate():
    print("Last modified: %s" % time.ctime(os.path.getmtime("C:/users/admin/Desktop/New Text Document.txt")))
    print("Created: %s" % time.ctime(os.path.getctime("C:/users/admin/Desktop/New Text Document.txt")))
    print("File Name: %s" % os.path.basename('C:/users/admin/Desktop/New Text Document.txt'))


ModifiedDate()

EMAIL_ADDRESS = 'EmailID'
EMAIL_PASSWORD = 'Password'

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

Part1 = "Please check the modified dates of the below LogFiles and take the action if needed. \n \n"
Part2 = "File Name: %s \n" % os.path.basename("C:/users/admin/Desktop/New Text Document.txt")
Part3 = "Last Modified: %s" % time.ctime(os.path.getmtime("C:/users/admin/Desktop/New Text Document.txt"))

subject = 'Modified LogFiles Date'
body = Part1 + Part2 + Part3

msg = f'Subject: {subject}\n\n{body}'

server.sendmail("SenderEmailID",
                "ReceiverEmailID",
                msg)

server.quit()

#'Please check the modified dates of the below LogFiles and take the action if needed'


# if time.ctime(os.path.getmtime("C:/users/admin/Desktop/New Text Document.txt")) < time.ctime(os.path.getctime("C:/users/admin/Desktop/New Text Document.txt")):
# print("Error")

# else:
#   print("all good")
