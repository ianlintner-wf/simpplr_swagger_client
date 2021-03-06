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

class AlertForSiteMembers(object):
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
        'message': 'str',
        'display_from': 'str',
        'segment_id': 'str',
        'is_dismissible': 'bool',
        'members_type': 'str',
        'has_url': 'bool',
        'recipient': 'str',
        'display_to': 'str'
    }

    attribute_map = {
        'site_id': 'siteId',
        'message': 'message',
        'display_from': 'displayFrom',
        'segment_id': 'segmentId',
        'is_dismissible': 'isDismissible',
        'members_type': 'membersType',
        'has_url': 'hasUrl',
        'recipient': 'recipient',
        'display_to': 'displayTo'
    }

    def __init__(self, site_id=None, message=None, display_from=None, segment_id=None, is_dismissible=None, members_type=None, has_url=None, recipient=None, display_to=None):  # noqa: E501
        """AlertForSiteMembers - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._message = None
        self._display_from = None
        self._segment_id = None
        self._is_dismissible = None
        self._members_type = None
        self._has_url = None
        self._recipient = None
        self._display_to = None
        self.discriminator = None
        self.site_id = site_id
        self.message = message
        self.display_from = display_from
        self.segment_id = segment_id
        self.is_dismissible = is_dismissible
        self.members_type = members_type
        self.has_url = has_url
        self.recipient = recipient
        self.display_to = display_to

    @property
    def site_id(self):
        """Gets the site_id of this AlertForSiteMembers.  # noqa: E501


        :return: The site_id of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this AlertForSiteMembers.


        :param site_id: The site_id of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def message(self):
        """Gets the message of this AlertForSiteMembers.  # noqa: E501


        :return: The message of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlertForSiteMembers.


        :param message: The message of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def display_from(self):
        """Gets the display_from of this AlertForSiteMembers.  # noqa: E501


        :return: The display_from of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._display_from

    @display_from.setter
    def display_from(self, display_from):
        """Sets the display_from of this AlertForSiteMembers.


        :param display_from: The display_from of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if display_from is None:
            raise ValueError("Invalid value for `display_from`, must not be `None`")  # noqa: E501

        self._display_from = display_from

    @property
    def segment_id(self):
        """Gets the segment_id of this AlertForSiteMembers.  # noqa: E501


        :return: The segment_id of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this AlertForSiteMembers.


        :param segment_id: The segment_id of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if segment_id is None:
            raise ValueError("Invalid value for `segment_id`, must not be `None`")  # noqa: E501

        self._segment_id = segment_id

    @property
    def is_dismissible(self):
        """Gets the is_dismissible of this AlertForSiteMembers.  # noqa: E501


        :return: The is_dismissible of this AlertForSiteMembers.  # noqa: E501
        :rtype: bool
        """
        return self._is_dismissible

    @is_dismissible.setter
    def is_dismissible(self, is_dismissible):
        """Sets the is_dismissible of this AlertForSiteMembers.


        :param is_dismissible: The is_dismissible of this AlertForSiteMembers.  # noqa: E501
        :type: bool
        """
        if is_dismissible is None:
            raise ValueError("Invalid value for `is_dismissible`, must not be `None`")  # noqa: E501

        self._is_dismissible = is_dismissible

    @property
    def members_type(self):
        """Gets the members_type of this AlertForSiteMembers.  # noqa: E501


        :return: The members_type of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._members_type

    @members_type.setter
    def members_type(self, members_type):
        """Sets the members_type of this AlertForSiteMembers.


        :param members_type: The members_type of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if members_type is None:
            raise ValueError("Invalid value for `members_type`, must not be `None`")  # noqa: E501

        self._members_type = members_type

    @property
    def has_url(self):
        """Gets the has_url of this AlertForSiteMembers.  # noqa: E501


        :return: The has_url of this AlertForSiteMembers.  # noqa: E501
        :rtype: bool
        """
        return self._has_url

    @has_url.setter
    def has_url(self, has_url):
        """Sets the has_url of this AlertForSiteMembers.


        :param has_url: The has_url of this AlertForSiteMembers.  # noqa: E501
        :type: bool
        """
        if has_url is None:
            raise ValueError("Invalid value for `has_url`, must not be `None`")  # noqa: E501

        self._has_url = has_url

    @property
    def recipient(self):
        """Gets the recipient of this AlertForSiteMembers.  # noqa: E501


        :return: The recipient of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this AlertForSiteMembers.


        :param recipient: The recipient of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def display_to(self):
        """Gets the display_to of this AlertForSiteMembers.  # noqa: E501


        :return: The display_to of this AlertForSiteMembers.  # noqa: E501
        :rtype: str
        """
        return self._display_to

    @display_to.setter
    def display_to(self, display_to):
        """Sets the display_to of this AlertForSiteMembers.


        :param display_to: The display_to of this AlertForSiteMembers.  # noqa: E501
        :type: str
        """
        if display_to is None:
            raise ValueError("Invalid value for `display_to`, must not be `None`")  # noqa: E501

        self._display_to = display_to

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
        if issubclass(AlertForSiteMembers, dict):
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
        if not isinstance(other, AlertForSiteMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
