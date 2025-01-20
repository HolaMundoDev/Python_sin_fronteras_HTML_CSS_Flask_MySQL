import sendgrid
from sendgrid.helpers.mail import *
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, current_app
)

from app.db import get_db
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

bp = Blueprint('mail', __name__, url_prefix='/')


@bp.route("/", methods=('GET', 'POST'))
def index():
    search = request.args.get('search')
    db, c = get_db()
    if search is None:
        mails = c.execute('SELECT * FROM email')
    else:
        mails = c.execute(
            'SELECT * FROM email WHERE content LIKE %s', ('%'+search+'%',))
    mails = c.fetchall()
    return render_template('mail/index.html', mails=mails)


@bp.route("/create", methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        email = request.form.get("email")
        subject = request.form.get("subject")
        content = request.form.get("content")
        errors = []

        if not email:
            errors.append("Email es obligatorio.")
        if not subject:
            errors.append("Subject es obligatorio.")
        if not content:
            errors.append("Content es obligatorio.")

        if len(errors) == 0:
            try:
                send(email, subject, content)
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                flash("Error al enviar el correo")
                return redirect(url_for('mail.index'))
            db, c = get_db()
            c.execute('INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)',
                      (email, subject, content))
            db.commit()

            return redirect(url_for('mail.index'))
        else:
            for error in errors:
                flash(error)

        print(email, subject, content)
    return render_template('mail/create.html')


# def send(to, subject, content):
#     sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
#     from_email = Email(current_app.config['FROM_EMAIL'])
#     to_email = To(to)
#     content = Content("text/plain", content)
#     mail = Mail(from_email, to_email, subject, content)
#     response = sg.client.mail.send.post(request_body=mail.get())
#     print(response)

def send(to, subject, content):
    msg = MIMEMultipart()
    msg['From'] = current_app.config['FROM_EMAIL']
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'plain'))
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()

        smtp.login(current_app.config["SMTP_USERNAME"], current_app.config["SMTP_PASSWORD"])
        smtp.send_message(msg)
        print("Mensaje enviado")

