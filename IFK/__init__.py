import os
from flask import Flask
from flask_restful import Api
from pony.orm import Database


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

api = Api(app, catch_all_404s=True)
db = Database()


from Models.models import Member, Section


DB_FILE = app.config['DB_FILE']

db.bind("sqlite", DB_FILE, create_db=True)
db.generate_mapping(create_tables=True)


from IFK.Resources.MemberAPI import Members, MemberAPI
from IFK.Resources.SectionApi import SectionAPI, SectionsAPI


