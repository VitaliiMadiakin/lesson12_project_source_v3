from flask import Blueprint, render_template

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/post_form.html')
def loader_page():
    return render_template('post_form.html')
