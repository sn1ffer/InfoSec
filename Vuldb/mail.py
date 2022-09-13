import os
import yaml
import smtplib
import result
import email.utils
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

mail_settings = yaml.load(open(os.path.abspath('mail_config.yaml')), Loader=yaml.FullLoader)

user = mail_settings['user']
passwd = mail_settings['passwd']
server = mail_settings['server']
port = mail_settings['port']
message = mail_settings['message']
subject = mail_settings['subject']
to = mail_settings['to']
filename = result.file



def send_mail(send_from, send_to, subject, file,
              server, port, password):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = email.utils.COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    part = MIMEBase('application', "octet-stream")
    with open(file, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="{}"'.format(op.basename(filename)))
    msg.attach(part)
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(send_from, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_mail(user, to, subject, filename, server, port, passwd)