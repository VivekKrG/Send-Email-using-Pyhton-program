# Send-Email-using-Pyhton-program
This repository contains programming file and documentation to send email through python program.

Reference: GeeksforGeeks
# Introduction
Python offers a native library to send emails- “SMTP lib”. “smtplib” creates a Simple Mail Transfer Protocol client session object which is used to send emails to any valid email id on the internet. Different websites use different port numbers.
# Steps to send mail from Gmail account

1. First of all, “smtplib” library needs to be imported.

2. After that, to create a session, we will be using its instance SMTP to encapsulate an SMTP connection.
s = smtplib.SMTP('smtp.gmail.com', 587)
In this, you need to pass the first parameter of the server location and the second parameter of the port to use. For Gmail, we use port number 587.

3. For security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands. After that, for security and authentication, you need to pass your Gmail account credentials in the login instance.
The compiler will show an authentication error if you enter invalid email id or password.

4. Store the message you need to send in a variable say, message. Using the sendmail() instance, send your message. sendmail() uses three parameters: sender_email_id, receiver_email_id and message_to_be_sent. The parameters need to be in the same sequence.

This will send the email from your account. After you have completed your task, terminate the SMTP session by using quit().

