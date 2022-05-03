from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

#Open Terminal on "Surfs Up" Folder
#Type - "export FLASK_APP=app.py" and press enter
#Type - "flask run" and press enter
# Last login: Tue May  3 08:27:52 on ttys002
# (base) brenton@brentons-mbp surfs_up % export FLASK_APP=app.py
# (base) brenton@brentons-mbp surfs_up % flask run
#  * Serving Flask app "app.py"
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## The Running on http://127.0.0.1:5000/ is the website, copy into chrome