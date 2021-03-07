from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse

from .models import Url

URL = "https://www.google.com/"


class TestUrlShortener(TestCase):
    def test_redirect_with_code(self):
        """
        Positive test case
        Calling url for non existing code should return 301 code
        """
        url = Url.objects.create(full_url=URL, code="shr")
        response = self.client.get(reverse("url:url-redirect", args=("shr",)))
        self.assertRedirects(
            response, url.full_url, status_code=301, fetch_redirect_response=False
        )

    def test_detail_view_with_existing_code(self):
        """
        Positive test case
        Detail for shortened URL with valid code should return 200 code
        """
        url = Url.objects.create(full_url=URL, code="shr")
        response = self.client.get(reverse("url:url-detail", args=("shr",)))
        self.assertContains(response, url.full_url, status_code=200)

    def test_redirect_with_non_existing_code(self):
        """
        Negative test case
        Calling url for non existing code should return 404 code
        """
        response = self.client.get(
            reverse("url:url-redirect", args=("non_existing_code",))
        )
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_non_existing_code(self):
        """
        Negative test case
        Detail for shortened URL with valid code should return 404 code
        """
        response = self.client.get(
            reverse("url:url-redirect", args=("non_existing_code",))
        )
        self.assertEqual(response.status_code, 404)

    def test_home_with_code(self):
        """
        Positive test case
        Newly created Url object should have full_url and code equal to those given in post request
        """
        response = self.client.post(
            reverse("url:url-home"), {"full_url": URL, "code": "ggl"}, follow=True
        )

        # get() throws DoesNotExist if it can't find object
        url = Url.objects.get(full_url=URL, code="ggl")
        self.assertEqual(url.full_url, URL)
        self.assertEqual(url.code, "ggl")

    def test_home_without_code(self):
        """
        Positive test case
        Newly created Url object should have full_url equal to this given in post request
        Code was not passed, so it should be generated automatically and different from None
        """
        response = self.client.post(
            reverse("url:url-home"), {"full_url": URL}, follow=True
        )

        # get() throws DoesNotExist if it can't find object
        url = Url.objects.get(full_url=URL)
        self.assertIsNotNone(url.code)

    def test_home_with_duplicate_code(self):
        """
        Negative test case
        Posting another Url with same code should result in displaying message with information about
        code being already taken
        """
        response_1 = self.client.post(
            reverse("url:url-home"), {"full_url": URL, "code": "ggl"}, follow=True
        )

        response_2 = self.client.post(
            reverse("url:url-home"), {"full_url": URL, "code": "ggl"}, follow=True
        )

        # get() throws MultipleObjectsReturned,  if it finds more than one object
        url = Url.objects.get(full_url=URL, code="ggl")
        self.assertContains(
            response_2,
            "This code is already taken, please type in another one or leave this field empty for autogenerated code",
        )

    def test_home_with_invalid_field_characters(self):
        """
        Negative test case
        Posting another Url with invalid character should not create object and return specific message
        """
        response = self.client.post(
            reverse("url:url-home"), {"full_url": URL, "code": "ggl@"}, follow=True
        )

        # get() throws DoesNotExist,  if it can't find object
        with self.assertRaises(ObjectDoesNotExist):
            Url.objects.get(full_url=URL, code="ggl@")
        self.assertContains(
            response,
            "Code can only contain hyphens, lowercase/uppercase letters, numbers and underscores",
        )
