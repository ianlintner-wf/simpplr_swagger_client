# coding: utf-8

"""
    Simpplr APIs

    This collection of Simpplr APIs lets developers create and manage content outside the Simpplr UI. We have APIs for notifications, alerts, app searches, and content creation. Looking for parameters or code samples? Click on an endpoint to see a sample snippet along with descriptions of its parameters and responses.  If you have questions about an API, reach out to us support@simpplr.com  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.alert_api import AlertApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alert_create(self):
        """Test case for alert_create

        Create an Alert For Everyone  # noqa: E501
        """
        pass

    def test_alert_create_for_site_members(self):
        """Test case for alert_create_for_site_members

        Create new alert for site members/ followers by site id  # noqa: E501
        """
        pass

    def test_delete_alert_by_id(self):
        """Test case for delete_alert_by_id

        Delete alert by ID  # noqa: E501
        """
        pass

    def test_edit_alert_by_id(self):
        """Test case for edit_alert_by_id

        Edit Alert By ID  # noqa: E501
        """
        pass

    def test_expire_alert_by_id(self):
        """Test case for expire_alert_by_id

        Expire alert by ID  # noqa: E501
        """
        pass

    def test_list_alerts(self):
        """Test case for list_alerts

        List Alerts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
