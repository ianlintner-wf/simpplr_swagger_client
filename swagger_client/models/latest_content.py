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

class LatestContent(object):
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
        'size': 'int',
        'site_id': 'str',
        'status': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'size': 'size',
        'site_id': 'siteId',
        'status': 'status',
        'filter': 'filter'
    }

    def __init__(self, size=None, site_id=None, status=None, filter=None):  # noqa: E501
        """LatestContent - a model defined in Swagger"""  # noqa: E501
        self._size = None
        self._site_id = None
        self._status = None
        self._filter = None
        self.discriminator = None
        if size is not None:
            self.size = size
        if site_id is not None:
            self.site_id = site_id
        if status is not None:
            self.status = status
        if filter is not None:
            self.filter = filter

    @property
    def size(self):
        """Gets the size of this LatestContent.  # noqa: E501


        :return: The size of this LatestContent.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LatestContent.


        :param size: The size of this LatestContent.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def site_id(self):
        """Gets the site_id of this LatestContent.  # noqa: E501


        :return: The site_id of this LatestContent.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this LatestContent.


        :param site_id: The site_id of this LatestContent.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def status(self):
        """Gets the status of this LatestContent.  # noqa: E501


        :return: The status of this LatestContent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LatestContent.


        :param status: The status of this LatestContent.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def filter(self):
        """Gets the filter of this LatestContent.  # noqa: E501


        :return: The filter of this LatestContent.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this LatestContent.


        :param filter: The filter of this LatestContent.  # noqa: E501
        :type: str
        """

        self._filter = filter

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
        if issubclass(LatestContent, dict):
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
        if not isinstance(other, LatestContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
