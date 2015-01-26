from flask import Flask
import flask_restful as rest

from IFK.Resources.MemberAPI import Members, MemberAPI
from IFK.Resources.SectionApi import SectionAPI, SectionsAPI
from IFK.Models import db

app = Flask(__name__)
api = rest.Api(app)

db.bind("sqlite", "ifkdb.sqlite", create_db=True)
db.generate_mapping(create_tables=True)

api.add_resource(Members, '/members')
api.add_resource(MemberAPI, '/member/<int:id>')
#api.add_resource(MemberAPI, '/member')
api.add_resource(SectionAPI, '/section/<code>')
api.add_resource(SectionsAPI, '/sections')







if __name__ == '__main__':

    app.run(debug=True)
    # app.run(debug=False)
