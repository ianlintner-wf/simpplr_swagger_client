# coding: utf-8

"""
    Simpplr APIs

    This collection of Simpplr APIs lets developers create and manage content outside the Simpplr UI. We have APIs for notifications, alerts, app searches, and content creation. Looking for parameters or code samples? Click on an endpoint to see a sample snippet along with descriptions of its parameters and responses.  If you have questions about an API, reach out to us support@simpplr.com  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SiteEditAnalytics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total_page_count': 'int',
        'total_event_count': 'int',
        'total_album_count': 'int',
        'csv_url': 'str'
    }

    attribute_map = {
        'total_page_count': 'totalPageCount',
        'total_event_count': 'totalEventCount',
        'total_album_count': 'totalAlbumCount',
        'csv_url': 'csvUrl'
    }

    def __init__(self, total_page_count=None, total_event_count=None, total_album_count=None, csv_url=None):  # noqa: E501
        """SiteEditAnalytics - a model defined in Swagger"""  # noqa: E501
        self._total_page_count = None
        self._total_event_count = None
        self._total_album_count = None
        self._csv_url = None
        self.discriminator = None
        if total_page_count is not None:
            self.total_page_count = total_page_count
        if total_event_count is not None:
            self.total_event_count = total_event_count
        if total_album_count is not None:
            self.total_album_count = total_album_count
        if csv_url is not None:
            self.csv_url = csv_url

    @property
    def total_page_count(self):
        """Gets the total_page_count of this SiteEditAnalytics.  # noqa: E501


        :return: The total_page_count of this SiteEditAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, total_page_count):
        """Sets the total_page_count of this SiteEditAnalytics.


        :param total_page_count: The total_page_count of this SiteEditAnalytics.  # noqa: E501
        :type: int
        """

        self._total_page_count = total_page_count

    @property
    def total_event_count(self):
        """Gets the total_event_count of this SiteEditAnalytics.  # noqa: E501


        :return: The total_event_count of this SiteEditAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_event_count

    @total_event_count.setter
    def total_event_count(self, total_event_count):
        """Sets the total_event_count of this SiteEditAnalytics.


        :param total_event_count: The total_event_count of this SiteEditAnalytics.  # noqa: E501
        :type: int
        """

        self._total_event_count = total_event_count

    @property
    def total_album_count(self):
        """Gets the total_album_count of this SiteEditAnalytics.  # noqa: E501


        :return: The total_album_count of this SiteEditAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_album_count

    @total_album_count.setter
    def total_album_count(self, total_album_count):
        """Sets the total_album_count of this SiteEditAnalytics.


        :param total_album_count: The total_album_count of this SiteEditAnalytics.  # noqa: E501
        :type: int
        """

        self._total_album_count = total_album_count

    @property
    def csv_url(self):
        """Gets the csv_url of this SiteEditAnalytics.  # noqa: E501


        :return: The csv_url of this SiteEditAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._csv_url

    @csv_url.setter
    def csv_url(self, csv_url):
        """Sets the csv_url of this SiteEditAnalytics.


        :param csv_url: The csv_url of this SiteEditAnalytics.  # noqa: E501
        :type: str
        """

        self._csv_url = csv_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SiteEditAnalytics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SiteEditAnalytics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other