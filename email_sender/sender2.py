import smtplib
from email.message import EmailMessage
from string import Template #will allow us to substitute # for the right wording
from pathlib import Path #similar to os.path

html = Template(Path('whereisindexhtmlpath').read_text())
email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'targetemail@address.com'
email['subject'] = 'subject of your email'

email.set_content(html.substitute({'name','Tin-Tin',}),'html')

email.set_content('Text of the email or body')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  #host
    smtp.ehlo() #look for the history of why it's not "hello" instead of ehlo
    smtp.starttls() #encryption mechanism to connect securily to the server
    smtp.login('senderemail','passwordofsenderssemail')
    smtp.send_message(email)
    print('all good boss!') #to make sure that it really worked. 

