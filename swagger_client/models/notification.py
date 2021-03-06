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

class Notification(object):
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
        'property_name': 'str',
        'sent_to': 'str',
        'sent_by': 'str',
        'url': 'str',
        'notification_type': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'property_name': 'propertyName',
        'sent_to': 'sentTo',
        'sent_by': 'sentBy',
        'url': 'url',
        'notification_type': 'notificationType',
        'comment': 'comment'
    }

    def __init__(self, property_name=None, sent_to=None, sent_by=None, url=None, notification_type=None, comment=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501
        self._property_name = None
        self._sent_to = None
        self._sent_by = None
        self._url = None
        self._notification_type = None
        self._comment = None
        self.discriminator = None
        self.property_name = property_name
        self.sent_to = sent_to
        self.sent_by = sent_by
        self.url = url
        if notification_type is not None:
            self.notification_type = notification_type
        if comment is not None:
            self.comment = comment

    @property
    def property_name(self):
        """Gets the property_name of this Notification.  # noqa: E501


        :return: The property_name of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this Notification.


        :param property_name: The property_name of this Notification.  # noqa: E501
        :type: str
        """
        if property_name is None:
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501

        self._property_name = property_name

    @property
    def sent_to(self):
        """Gets the sent_to of this Notification.  # noqa: E501


        :return: The sent_to of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._sent_to

    @sent_to.setter
    def sent_to(self, sent_to):
        """Sets the sent_to of this Notification.


        :param sent_to: The sent_to of this Notification.  # noqa: E501
        :type: str
        """
        if sent_to is None:
            raise ValueError("Invalid value for `sent_to`, must not be `None`")  # noqa: E501

        self._sent_to = sent_to

    @property
    def sent_by(self):
        """Gets the sent_by of this Notification.  # noqa: E501


        :return: The sent_by of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._sent_by

    @sent_by.setter
    def sent_by(self, sent_by):
        """Sets the sent_by of this Notification.


        :param sent_by: The sent_by of this Notification.  # noqa: E501
        :type: str
        """
        if sent_by is None:
            raise ValueError("Invalid value for `sent_by`, must not be `None`")  # noqa: E501

        self._sent_by = sent_by

    @property
    def url(self):
        """Gets the url of this Notification.  # noqa: E501


        :return: The url of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Notification.


        :param url: The url of this Notification.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def notification_type(self):
        """Gets the notification_type of this Notification.  # noqa: E501


        :return: The notification_type of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this Notification.


        :param notification_type: The notification_type of this Notification.  # noqa: E501
        :type: str
        """

        self._notification_type = notification_type

    @property
    def comment(self):
        """Gets the comment of this Notification.  # noqa: E501


        :return: The comment of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Notification.


        :param comment: The comment of this Notification.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
