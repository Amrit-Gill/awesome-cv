# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
from models.details import Details  # noqa: F401,E501
import util


class ExperienceItems(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, company: str=None, title: str=None, address: str=None, start_date: date=None, end_date: date=None, details: List[Details]=None):  # noqa: E501
        """ExperienceItems - a model defined in Swagger

        :param company: The company of this ExperienceItems.  # noqa: E501
        :type company: str
        :param title: The title of this ExperienceItems.  # noqa: E501
        :type title: str
        :param address: The address of this ExperienceItems.  # noqa: E501
        :type address: str
        :param start_date: The start_date of this ExperienceItems.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this ExperienceItems.  # noqa: E501
        :type end_date: date
        :param details: The details of this ExperienceItems.  # noqa: E501
        :type details: List[Details]
        """
        self.swagger_types = {
            'company': str,
            'title': str,
            'address': str,
            'start_date': date,
            'end_date': date,
            'details': List[Details]
        }

        self.attribute_map = {
            'company': 'company',
            'title': 'title',
            'address': 'address',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'details': 'details'
        }

        self._company = company
        self._title = title
        self._address = address
        self._start_date = start_date
        self._end_date = end_date
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'ExperienceItems':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The experienceItems of this ExperienceItems.  # noqa: E501
        :rtype: ExperienceItems
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company(self) -> str:
        """Gets the company of this ExperienceItems.


        :return: The company of this ExperienceItems.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company: str):
        """Sets the company of this ExperienceItems.


        :param company: The company of this ExperienceItems.
        :type company: str
        """

        self._company = company

    @property
    def title(self) -> str:
        """Gets the title of this ExperienceItems.


        :return: The title of this ExperienceItems.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ExperienceItems.


        :param title: The title of this ExperienceItems.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def address(self) -> str:
        """Gets the address of this ExperienceItems.


        :return: The address of this ExperienceItems.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this ExperienceItems.


        :param address: The address of this ExperienceItems.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def start_date(self) -> date:
        """Gets the start_date of this ExperienceItems.


        :return: The start_date of this ExperienceItems.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this ExperienceItems.


        :param start_date: The start_date of this ExperienceItems.
        :type start_date: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this ExperienceItems.


        :return: The end_date of this ExperienceItems.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this ExperienceItems.


        :param end_date: The end_date of this ExperienceItems.
        :type end_date: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def details(self) -> List[Details]:
        """Gets the details of this ExperienceItems.


        :return: The details of this ExperienceItems.
        :rtype: List[Details]
        """
        return self._details

    @details.setter
    def details(self, details: List[Details]):
        """Sets the details of this ExperienceItems.


        :param details: The details of this ExperienceItems.
        :type details: List[Details]
        """

        self._details = details
