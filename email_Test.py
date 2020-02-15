'''
Sending email from Python Script.
'''


import smtplib
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) # 25 also works
  
# start TLS for security 
s.starttls() 
from_email = "vivekkumarguptalucky@gmail.com" #"eknowledgec@gmail.com"
from_email_pass = "password do"
receiver_email = "eknowledgec@gmail.com" #"vivekkumarguptalucky@gmail.com"
# Authentication 
s.login(from_email, from_email_pass) 
  
# message to be sent 
message = "Hello Message from python script Vivek Kumar from port 25"
  
# sending the mail 
s.sendmail(from_email, receiver_email, message) 
  
# terminating the session 
s.quit()
