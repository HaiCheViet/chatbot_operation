import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os,datetime

CRLF = "\r\n"
login = "chehaitest@gmail.com"
password = "Haipro!23"
# attendees = ["cheviethai123@gmail.com"]
organizer = "ORGANIZER;CN=organiser:mailto:first" + CRLF + " @gmail.com"
fro = "haitest che <chehaitest@gmail.com>"


def send_invitation(ddtstart, dtoff, target_mem):
    # ddtstart = datetime.datetime.now()
    # dtoff = datetime.timedelta(days=1)
    dur = datetime.timedelta(hours=1)
    ddtstart = ddtstart + dtoff
    dtend = ddtstart + dur
    dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

    description = "DESCRIPTION: test invitation from pyICSParser" + CRLF
    attendee = ""
    for att in target_mem:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + att + ";X-NUM-GUESTS=0:" + CRLF + " mailto:" + att + CRLF
    ical = "BEGIN:VCALENDAR" + CRLF + "PRODID:pyICSParser" + CRLF + "VERSION:2.0" + CRLF + "CALSCALE:GREGORIAN" + CRLF
    ical += "METHOD:REQUEST" + CRLF + "BEGIN:VEVENT" + CRLF + "DTSTART:" + dtstart + CRLF + "DTEND:" + dtend + CRLF + "DTSTAMP:" + dtstamp + CRLF + organizer + CRLF
    ical += "UID:FIXMEUID" + dtstamp + CRLF
    ical += attendee + "CREATED:" + dtstamp + CRLF + description + "LAST-MODIFIED:" + dtstamp + CRLF + "LOCATION:" + CRLF + "SEQUENCE:0" + CRLF + "STATUS:CONFIRMED" + CRLF
    ical += "SUMMARY:test " + ddtstart.strftime(
        "%Y%m%d @ %H:%M") + CRLF + "TRANSP:OPAQUE" + CRLF + "END:VEVENT" + CRLF + "END:VCALENDAR" + CRLF

    eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
    eml_body_bin = "This is the email body in binary - two steps"
    msg = MIMEMultipart('mixed')
    msg['Reply-To'] = fro
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "pyICSParser invite" + dtstart
    msg['From'] = fro
    msg['To'] = ",".join(target_mem)

    part_email = MIMEText(eml_body, "html")
    part_cal = MIMEText(ical, 'calendar;method=REQUEST')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics', ' ;name="%s"' % ("invite.ics"))
    ical_atch.set_payload(ical)
    Encoders.encode_base64(ical_atch)
    ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"' % ("invite.ics"))

    eml_atch = MIMEBase('text/plain', '')
    Encoders.encode_base64(eml_atch)
    eml_atch.add_header('Content-Transfer-Encoding', "")

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(login, password)
    mailServer.sendmail(fro, target_mem, msg.as_string())
    mailServer.close()
    return "Done send invitation"

def send_content(content, target_mem):
    msg = MIMEMultipart()
    message = content

    msg['Subject'] = "test"
    msg['From'] = fro
    msg['To'] = ",".join(target_mem)
    msg.attach(MIMEText(message, 'plain'))

    # Send the message via our own SMTP server.
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.starttls()
    mailServer.login(login, password)

    mailServer.sendmail(fro, target_mem, msg.as_string())

    mailServer.quit()
    return "Done send message to %s" %target_mem

# def send_reminder()

if __name__ == "__main__":
    mess = """
    Dear bro, 

    This is a test message. 
    Have a great weekend! 
    
    Yours Truly
    """
    print(send_content(mess, ["cheviethai123@gmail.com"]))



