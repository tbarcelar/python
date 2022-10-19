import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'outlook.office365.com'
port = 587
user = 'xxxxxr@hotmail.com'
password = 'xxxxxxxxxx'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = ' essa é a mensagem do e-mail'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'xxxxxxx@gmail.com'
email_msg['Subject'] = 'esse é o titulo'
print('enviando o e-mail - aguarde ')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()