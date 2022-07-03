from flask import Blueprint, render_template, request
from flask_security import auth_required
from flask_security import current_user, auth_required
upload_pages = Blueprint("upload_pages", __name__, url_prefix='/upload')


@upload_pages.route("/")
@auth_required()
def upload():
    if request.method == "POST":
        # Receiving an image
        pass

    return render_template("upload.html")
    