import json
from flask import request
from pony.orm import db_session, select,commit, ObjectNotFound, IntegrityError
import flask.ext.restful as rest
from IFK.Models.models import Section


class SectionAPI(rest.Resource):

    def get(self, code):
        with db_session:                                   
            section = Section[code]

            if section is None:
                return {'error': "section not found"}, 404

            return {
                "code": code,
                "name": section.name,
                "leader": section.leader.name
                }, 200


    def put(self, code):
        pass

    def delete(self, code):
        pass

class SectionsAPI(rest.Resource):

    def get(self):
        with db_session:
            result = {}
            for section in select(section for section in Section):
                result[section.code] = {'name': section.name, 'leader': section.leader.name}
            return result



    def put(self):
        data = json.loads(request.data)
        try:
            code = data['code']
            name = data['name']
            leader = data['leader']
        except KeyError as e:
            return {'error': "Bad request2", "errors": "%s" % e}
        try:
            with db_session:
                section = Section(code=code, leader=leader, name=name)
                commit()
        except Exception as e:
            return {"error": str(e)}

        return {'new':'section:%s' % section.code}

