from flask import (
    Blueprint, render_template
    )

from app.db import get_db

bp = Blueprint('mail', __name__, url_prefix='/')
@bp.route("/", methods=('GET', 'POST'))
def index():
    db, c = get_db()
    mails = c.execute('SELECT * FROM email')
    mails = c.fetchall()

    return render_template('mail/index.html', mails=mails)

@bp.route("/create", methods=('GET', 'POST'))
def create():
    return render_template('mail/create.html')
