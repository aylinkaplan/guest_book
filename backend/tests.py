from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from backend.models import GuestBook


class GuestBookTests(APITestCase):
    def setUp(self):
        self.user = User(username="test")
        password = 'test'
        self.user.set_password(password)
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client = APIClient()
        self.client.login(username=self.user.username, password=password)

    def test_guestbook_list(self):
        GuestBook.objects.create(
            name="Guest Book 1", subject="Guest Book 1 Description", message="Guest Book 1 Message")
        GuestBook.objects.create(
            name="Guest Book 2", subject="Guest Book 2 Description", message="Guest Book 1 Message")
        GuestBook.objects.create(
            name="Guest Book 3", subject="Guest Book 3 Description", message="Guest Book 1 Message")
        response = self.client.get("/api/list/", HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_guestbook_detail(self):
        guestbook = GuestBook.objects.create(
            name="Guest Book 1", subject="Guest Book 1 Description", message="Guest Book 1 Message")
        response = self.client.get(f'/api/list/{guestbook.id}/', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_guestbook_delete(self):
        guestbook = GuestBook.objects.create(
            name="Guest Book 1", subject="Guest Book 1 Description", message="Guest Book 1 Message")
        response = self.client.delete(f"/api/delete/{guestbook.id}/", HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_guestbook_update(self):
        guestbook = GuestBook.objects.create(
            name="Guest Book 1", subject="Guest Book 1 Description", message="Guest Book 1 Message")
        data = {"name": "Guest Book 1", "subject": "Guest Book 2 Description", "message": "Guest Book 2 Message"}
        response = self.client.put(f'/api/update/{guestbook.id}/', data=data,
                                   HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
