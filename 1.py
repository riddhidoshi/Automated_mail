import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr='riddhidoshi771@gmail.com'
to_addr=['riddhi.bca2021@gmail.com','sitaldoshi@gmail.com']
msg=MIMEMultipart()
msg['Form']=from_addr
msg['To']=",".join(to_addr)
msg['subject']='just to check'

body='hello world'

msg.attach(MIMEText(body,'plain'))

email="riddhidoshi771@gmail.com"
password="rsiudbdhhaim@1811"

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()
