from flask import Blueprint, render_template

route_account = Blueprint("account_page", __name__)


@route_account.route("/index")
def index():
    return render_template('account/index.html')