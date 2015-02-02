import json
from pony.orm import db_session, select, commit, ObjectNotFound
import flask.ext.restful as rest

from IFK.Models.models import Member
from IFK import api

from flask import request, abort



@api.resource('/member/<int:id>')
class MemberAPI(rest.Resource):

    def get(self, id):

        with db_session:
            member = Member[id]

            if member is None:
                return abort(404)

            return {
                "id": id,
                "name": member.name,
                "phone": member.phone
            }, 200

    def put(self, id):

        name = request.json.get('name', None)
        phone = request.json.get("phone", None)



        with db_session:
            member = Member[id]

            if not member:
                return abort(404)
            else:
                if name:
                    member.name = name
                if phone:
                    member.phone = phone

            return {"member": "updated"}, 202

    def delete(self, id):

        with db_session:
            member = Member[id]
            if member is None:
                abort(404)
            member.delete()

        return {"delete": "member %s" % id}, 200

@api.resource('/members')
class Members(rest.Resource):
    def get(self):
        with db_session:
            result = {}
            for member in select(member for member in Member):
                result[member.id] = {'name': member.name, 'phone': member.phone}

            return result



    def put(self):




        if request.json is None:
            return abort(415)


        try:
            name = request.json['name']
            phone = request.json.get("phone", None)  #optional
        except KeyError, e:
            return abort(400)



        with db_session:
            member = Member(name=name, phone=phone)
            commit()

            return {"id": member.id, "name": member.name, "phone": member.phone}, 201










