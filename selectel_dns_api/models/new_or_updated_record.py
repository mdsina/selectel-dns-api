# coding: utf-8

"""
    Selectel DNS API

    Simple Selectel DNS API.

    OpenAPI spec version: 1.0.1
    Contact: info@mdsina.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NewOrUpdatedRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'type': 'str',
        'ttl': 'int',
        'email': 'str',
        'content': 'str',
        'location': 'str',
        'weight': 'int',
        'port': 'int',
        'target': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'ttl': 'ttl',
        'email': 'email',
        'content': 'content',
        'location': 'location',
        'weight': 'weight',
        'port': 'port',
        'target': 'target',
        'priority': 'priority'
    }

    def __init__(self, name=None, type=None, ttl=None, email=None, content=None, location=None, weight=None, port=None, target=None, priority=None):
        """
        NewOrUpdatedRecord - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._ttl = None
        self._email = None
        self._content = None
        self._location = None
        self._weight = None
        self._port = None
        self._target = None
        self._priority = None

        self.name = name
        self.type = type
        if ttl is not None:
          self.ttl = ttl
        if email is not None:
          self.email = email
        if content is not None:
          self.content = content
        if location is not None:
          self.location = location
        if weight is not None:
          self.weight = weight
        if port is not None:
          self.port = port
        if target is not None:
          self.target = target
        if priority is not None:
          self.priority = priority

    @property
    def name(self):
        """
        Gets the name of this NewOrUpdatedRecord.

        :return: The name of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NewOrUpdatedRecord.

        :param name: The name of this NewOrUpdatedRecord.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this NewOrUpdatedRecord.
        Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF)

        :return: The type of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NewOrUpdatedRecord.
        Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF)

        :param type: The type of this NewOrUpdatedRecord.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def ttl(self):
        """
        Gets the ttl of this NewOrUpdatedRecord.

        :return: The ttl of this NewOrUpdatedRecord.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this NewOrUpdatedRecord.

        :param ttl: The ttl of this NewOrUpdatedRecord.
        :type: int
        """

        self._ttl = ttl

    @property
    def email(self):
        """
        Gets the email of this NewOrUpdatedRecord.
        Email of domain's admin (only for SOA records)

        :return: The email of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this NewOrUpdatedRecord.
        Email of domain's admin (only for SOA records)

        :param email: The email of this NewOrUpdatedRecord.
        :type: str
        """

        self._email = email

    @property
    def content(self):
        """
        Gets the content of this NewOrUpdatedRecord.
        Record content (not for SRV)

        :return: The content of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this NewOrUpdatedRecord.
        Record content (not for SRV)

        :param content: The content of this NewOrUpdatedRecord.
        :type: str
        """

        self._content = content

    @property
    def location(self):
        """
        Gets the location of this NewOrUpdatedRecord.

        :return: The location of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this NewOrUpdatedRecord.

        :param location: The location of this NewOrUpdatedRecord.
        :type: str
        """

        self._location = location

    @property
    def weight(self):
        """
        Gets the weight of this NewOrUpdatedRecord.
        Relative weight for records with the same priority (only for SRV)

        :return: The weight of this NewOrUpdatedRecord.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this NewOrUpdatedRecord.
        Relative weight for records with the same priority (only for SRV)

        :param weight: The weight of this NewOrUpdatedRecord.
        :type: int
        """

        self._weight = weight

    @property
    def port(self):
        """
        Gets the port of this NewOrUpdatedRecord.
        Service port (only for SRV)

        :return: The port of this NewOrUpdatedRecord.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this NewOrUpdatedRecord.
        Service port (only for SRV)

        :param port: The port of this NewOrUpdatedRecord.
        :type: int
        """

        self._port = port

    @property
    def target(self):
        """
        Gets the target of this NewOrUpdatedRecord.
        Service hostname (only for SRV)

        :return: The target of this NewOrUpdatedRecord.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this NewOrUpdatedRecord.
        Service hostname (only for SRV)

        :param target: The target of this NewOrUpdatedRecord.
        :type: str
        """

        self._target = target

    @property
    def priority(self):
        """
        Gets the priority of this NewOrUpdatedRecord.
        Record priority (only for SRV and MX records)

        :return: The priority of this NewOrUpdatedRecord.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this NewOrUpdatedRecord.
        Record priority (only for SRV and MX records)

        :param priority: The priority of this NewOrUpdatedRecord.
        :type: int
        """

        self._priority = priority

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NewOrUpdatedRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
