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

    def add_section_member(self, code, member_id):
        data = json.dumps({"code": code, "name": name})
        response = self.app.put('/section/%s/members', data=data, content_type='application/json')

        return json.loads(response.data), response.status_code
    def test_add_section_members(self):

        #add leader member
        response,status = self.add_member("bosse")
        member_id = response['id']
        #add section
        response,status = self.add_section(code="A", name="bosse", leader=member_id)






if __name__ == '__main__':
    unittest.main()