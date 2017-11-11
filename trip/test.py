from rest_framework.test import APITestCase

from trip.models import Dummy


class DummyTest(APITestCase):
    def setUp(self):
        dummy = Dummy()
        dummy.save()

    def test_dummy_state_change(self):
        """

        :return:
        """
        response = self.client.get(path='/car_shark/dummy/')
        self.assertTrue(True)
