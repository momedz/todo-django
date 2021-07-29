from django.test import TestCase, Client
import json


class ControllerTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_create(self):
        todo = {
            "title": "Feed cat",
            "description": "don't forgot"
        }

        response = self.client.post('/todo/', data=todo, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = json.loads(str(response.content, encoding='utf8'))
        fields = response[0]["fields"]
        self.assertEqual(fields, fields | todo)

    def test_get_all(self):
        todo = {
            "title": "Feed dog",
            "description": "don't forgot"
        }

        self.client.post('/todo/', data=todo, content_type="application/json")
        response = json.loads(str(self.client.get('/todo/').content, encoding='utf8'))

        self.assertEqual(response.__len__(), 1)
        fields = response[0]['fields']
        self.assertEqual(fields, fields | todo)

    def test_delete_all(self):
        todo = {
            "title": "Feed dog",
            "description": "don't forgot"
        }
        self.client.post('/todo/', data=todo, content_type="application/json")
        self.client.post('/todo/', data=todo, content_type="application/json")

        response = json.loads(str(self.client.get('/todo/').content, encoding='utf8'))
        self.assertEqual(response.__len__(), 2)

        response = json.loads(str(self.client.delete('/todo/').content, encoding='utf8'))
        self.assertEqual(response.__len__(), 0)

    def test_get_by_id(self):
        todo = {
            "title": "Feed dog",
            "description": "don't forgot"
        }
        self.client.post('/todo/', data=todo, content_type="application/json")

        response = json.loads(str(self.client.get('/todo/1/').content, encoding='utf8'))
        self.assertEqual(response.__len__(), 1)
        fields = response[0]['fields']
        self.assertEqual(fields, fields | todo)

    def test_update_by_id(self):
        todo = {
            "title": "Feed dog",
            "description": "don't forgot"
        }
        self.client.post('/todo/', data=todo, content_type="application/json")

        response = self.client.put('/todo/1/', data={
            "title": "Feed cat",
            "description": "don't forgot"
        }, content_type="application/json")
        response = json.loads(str(response.content, encoding='utf8'))
        fields = response[0]['fields']
        self.assertNotEqual(fields, fields | todo)
        self.assertEqual(fields, fields | todo | {
            "title": "Feed cat"
        })

    def test_delete_by_id(self):
        todo = {
            "title": "Feed dog",
            "description": "don't forgot"
        }
        self.client.post('/todo/', data=todo, content_type="application/json")
        self.client.post('/todo/', data=todo, content_type="application/json")

        response = json.loads(str(self.client.get('/todo/').content, encoding='utf8'))
        self.assertEqual(response.__len__(), 2)

        self.client.delete('/todo/1/')

        response = json.loads(str(self.client.get('/todo/').content, encoding='utf8'))
        self.assertEqual(response.__len__(), 1)


