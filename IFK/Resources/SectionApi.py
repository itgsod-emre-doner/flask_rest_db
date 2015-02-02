import json
from pony.orm import db_session, select, commit
import flask.ext.restful as rest

from IFK.Models.models import Section, Member
from IFK import api

from flask import request, abort


@api.resource('/section/<string:code>')
class SectionAPI(rest.Resource):

    def get(self, code):
        with db_session:                                   
            section = Section[code]

            if section is None:
                return {'error': "section not found"}, 404

            return {"status": 200, "message":
                {
                    "code": code,
                    "name": section.name,
                    "leader": section.leader.name
                }}, 200



    def put(self, code):
        pass

    def delete(self, code):
        pass


@api.resource('/sections')
class SectionsAPI(rest.Resource):

    def get(self):
        with db_session:
            result = {}
            for section in select(section for section in Section):
                result[section.code] = {'name': section.name, 'leader': section.leader.name}
            return {"status": 200, "message": result}, 200

    def put(self):
        data = json.loads(request.data)
        try:
            code = data['code']
            name = data['name']
            leader = data['leader']
        except KeyError as e:
            return abort(400)
        try:
            with db_session:
                section = Section(code=code, leader=leader, name=name)
                commit()
                leader = section.leader.name
        except Exception as e:
            return {"error": str(e)}

        return {"status": 201, "message": {"code": code, "name": name, "leader": leader}}, 201

@api.resource('/sectionx/<string:code>/members')
class MemberBySectionsAPI(rest.Resource):

    def get(self, code):

        with db_session:
            section=Section[code]
            if section is None:
                abort(404)

            result = {"Section:": section.name,}

            members={}
            for member in section.members:
                members[member.id] = {"name": member.name}

            result['members'] = members

            return result

    def put(self, code):
        with db_session:
            section=Section[code]
            if section is None:
                abort(404)

            member_id = request.json.get('member')

            try:
                section.members.add(Member[member_id])
            except Exception as e:
                return str(e)


            return "add member", 201




    def delete(self, code):
        with db_session:
            section=Section[code]
            if section is None:
                abort(404)

            member_id = request.json.get('member', None)

            section.members.add(Member[member_id])

            return "Ok", 201
