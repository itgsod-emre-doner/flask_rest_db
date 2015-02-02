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

    def delete_member(self, id):

        response = self.app.delete('/member/%s' % id)

        return json.loads(response.data), response.status_code

    def get_member(self, id):
        response = self.app.get('/member/%s' % id)

        return json.loads(response.data), response.status_code

    def get_members(self):
        response = self.app.get('/members')

        return json.loads(response.data), response.status_code


    def test_workflow(self):

        #add member "bosse"
        name = "bosse"
        response, status = self.add_member(name)
        id = response['id']

        self.assertEqual(status, 201)

        #get member with id should give name is "bosse"

        response, status = self.get_member(id)

        self.assertEqual(response['name'], name)
        self.assertEqual(status, 200)

        #get members with id should give name is "bosse"

        response, status = self.get_members()

        self.assertEqual(response[str(id)]['name'], name)
        self.assertEqual(status, 200)


        #delete member
        response, status = self.delete_member(id)

        self.assertEqual(status, 200)

        #get member

        response, status = self.get_member(id)

        self.assertEqual(status, 404)

    def test_404(self):

        response = self.app.get('/missing')

        data=json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)

    def test_415(self):

        response = self.app.put('/members')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 415)
        self.assertEqual(data['status'], 415)

    def test_405(self):

        response = self.app.post('/members')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['status'], 405)


if __name__ == '__main__':
    unittest.main()