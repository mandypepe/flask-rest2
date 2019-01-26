
from flask import *
def page_index():
    return render_template('index.html',select_menu="index")

#def init_website_routes(app):
    #if app:
        #app.add_url_rule('/about','page_about',page_about,methods=['GET'])
