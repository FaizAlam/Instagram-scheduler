#from crypt import methods
from fileinput import filename
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_security import auth_required
from flask_security import current_user, auth_required
import os
from b2_upload import upload_to_b2
from werkzeug.utils import secure_filename
from models import InstagramImage
from database import db_session

upload_pages = Blueprint("upload_pages", __name__, url_prefix='/upload')
UPLOAD_FOLDER = '/static'

@upload_pages.route("/", methods=['GET', 'POST'])
@auth_required()
def upload():
    if request.method == "POST":
        # Receiving an image

        if 'file' not in request.files:
            flash("No file part")
        file = request.files['image']
        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)
        
        name_file = file.filename
        file_ext = os.path.splitext(name_file)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            flash("Wrong extension")
            return redirect(request.url)
        print(name_file)
        file.save(name_file)
        # upload to bucket
        file_url = upload_to_b2(name_file)
        # delete image from local
        os.remove(name_file)

        db_session.add(InstagramImage(user_id= current_user.id, image_url = file_url))
        db_session.commit()

        return redirect(url_for(".upload"))
    return render_template("upload.html")
    