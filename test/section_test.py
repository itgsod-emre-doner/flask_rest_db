# -*- coding: UTF-8 -*-

import os
import unittest
import sys
import json

sys.path.append("../IFK")

os.environ['APP_SETTINGS'] = "config.TestingConfig"

from IFK import app



class TestCase(unittest.TestCase):
    def setUp(self):

        self.app = app.test_client()


    def add_member(self, name, phone=None):

        data = json.dumps({"name": name,"phone": phone})
        response = self.app.put('/members', data=data, content_type='application/json')

        return json.loads(response.data), response.status_code


    def add_section(self, code, name,leader):
        data = json.dumps({"code": code, "name": name, "leader": leader})
        response = self.app.put('/sections', data=data, content_type='application/json')

        return json.loads(response.data), response.status_code


    def delete_section(self, section_code):

        response = self.app.delete('/member/%s' % id)

        return json.loads(response.data), response.status_code

    def update_section_leader(self, section_code, member_id):
        response = self.app.get('/member/%s' % id)

        return json.loads(response.data), response.status_code

    def add_section_member(self, section_code, member_id):
        response = self.app.get('/section/%s' % section_code)


    def get_section(self, code):
        response = self.app.get('/section/%s' % code)

        return json.loads(response.data), response.status_code


    def get_sections(self):
        response = self.app.get('/sections')

        return json.loads(response.data), response.status_code


    def test_workflow(self):

        #if we haven't any sections
        response, status = self.get_sections()

        print response

        #add bosse as member"
        name = "bosse"
        response, status = self.add_member(name)
        id = int(response['id'])


        #add section brottning and add "bosse as leader"
        code="A"
        section_name = "brottning"

        response, status = self.add_section(code, name=section_name, leader=id)
        #response data should be equal to

        data = {"status": 201, "message": {"code": "A", "name": "brottning", "leader": "bosse"}}
        self.assertEqual(response, data)


        self.assertEqual(status, 201)


        #and we should get it with

        response, status = self.get_section(code)
        data = {"status": 200, "message": {"code": "A", "name": "brottning", "leader": "bosse"}}

        self.assertEqual(response, data)
        self.assertEqual(status, 200)






if __name__ == '__main__':
    unittest.main()