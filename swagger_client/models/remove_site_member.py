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

class RemoveSiteMember(object):
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
        'site_id': 'str',
        'sf_user_id': 'str'
    }

    attribute_map = {
        'site_id': 'siteId',
        'sf_user_id': 'sfUserId'
    }

    def __init__(self, site_id=None, sf_user_id=None):  # noqa: E501
        """RemoveSiteMember - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._sf_user_id = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        if sf_user_id is not None:
            self.sf_user_id = sf_user_id

    @property
    def site_id(self):
        """Gets the site_id of this RemoveSiteMember.  # noqa: E501


        :return: The site_id of this RemoveSiteMember.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this RemoveSiteMember.


        :param site_id: The site_id of this RemoveSiteMember.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def sf_user_id(self):
        """Gets the sf_user_id of this RemoveSiteMember.  # noqa: E501


        :return: The sf_user_id of this RemoveSiteMember.  # noqa: E501
        :rtype: str
        """
        return self._sf_user_id

    @sf_user_id.setter
    def sf_user_id(self, sf_user_id):
        """Sets the sf_user_id of this RemoveSiteMember.


        :param sf_user_id: The sf_user_id of this RemoveSiteMember.  # noqa: E501
        :type: str
        """

        self._sf_user_id = sf_user_id

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
        if issubclass(RemoveSiteMember, dict):
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
        if not isinstance(other, RemoveSiteMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other