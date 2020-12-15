import pytest
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase
from .models import MyUser

class AccountTests(APITestCase):


    def test_create_account(self):
        """
        POST to signup to create users.
        """
        response = self.client.post("http://localhost:8000/api/signup/",
                                    data={"username": "tests", "password": "TestTest"})
        first_user = MyUser.objects.get()
        self.assertEqual(response.status_code,  HTTP_201_CREATED)
        self.assertEqual(first_user.username, 'tests')
        response = self.client.post("http://localhost:8000/api/signup/",
                                    data={"username": "tests2", "password": "TestTest"})
        self.assertEqual(response.status_code,  HTTP_201_CREATED)
        self.assertTrue(MyUser.objects.filter(username="tests2").exists())
        user = MyUser.objects.get(username="tests2")
        response = self.client.put(f"http://localhost:8000/api/users/{user.pk}/", data={"email": "tst@test.te"})
        # Not logged shouldnt change anything
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
        user.set_password("TestTest")
        user.save()
        self.assertTrue(self.client.login(username="tests2", password="TestTest"))
        response = self.client.patch(f"http://localhost:8000/api/users/{user.pk}/", data={"email": "tst@test.te"})
        # Logged, should change
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(MyUser.objects.get(username="tests2").email, "tst@test.te")
        # Dont update others users
        response = self.client.patch(f"http://localhost:8000/api/users/{first_user.pk}/", data={"email": "tst@test.te"})
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

