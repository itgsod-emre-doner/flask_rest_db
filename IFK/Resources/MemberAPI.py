import json
from pony.orm import db_session, select, commit, ObjectNotFound
import flask.ext.restful as rest

from IFK.Models.models import Member


from flask import request


class MemberAPI(rest.Resource):

    def get(self, id):

        with db_session:
            member = Member[id]

            if member is None:
                return {'error': "member not found"}, 404

            return {
                "id": id,
                "name": member.name,
                "phone": member.phone
            }, 200

    def put(self, id):
        data = json.loads(request.data)

        try:
            name = data['name']
            phone = data['phone']
        except KeyError, e:
            return {'error': "Bad request"}, 400

        with db_session:
            member = Member[id]

            if not member:
                return {'error': "not found"}, 404
            else:
                member.name = name
                member.phone = phone

            return {"member": "updated"}, 202

    def delete(self,id):

        try:
            with db_session:
                member = Member[id]
                member.delete()
        except ObjectNotFound:
            return {'error': 'member not found'}

        return {"delete": "member %s" % id}


class Members(rest.Resource):
    def get(self):
        with db_session:
            result = {}
            for member in select(member for member in Member):
                result[member.id] = {'name': member.name, 'phone': member.phone}
            return result

    def put(self):

        try:
            name = request.json['name']
            phone = request.json.get("phone",None)
        except KeyError, e:
            return {'error': "Bad request"}, 400

        with db_session:
            member_id = Member(name=name, phone=phone)
            commit()

        return str(member_id)










