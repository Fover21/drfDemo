#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/10/21

from rest_framework.serializers import Field


class ImgPathField(Field):

    def __init__(self, prefix="", *args, **kwargs):

        super(ImgPathField, self).__init__(*args, **kwargs)
        self.prefix = prefix

    def to_internal_value(self, data):
        if not data:
            return None

        return data

    def to_representation(self, value):

        return "{}{}".format(self.prefix, value)

