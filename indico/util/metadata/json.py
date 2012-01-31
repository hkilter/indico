# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2012 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico;if not, see <http://www.gnu.org/licenses/>.

"""
simplejson-based fossil serializer
"""
# indico imports
from indico.util import json

# module imports
from indico.util.metadata.serializer import Serializer


class JSONSerializer(Serializer):

    """
    Does basically direct translation from the fossi
    """

    _mime = 'application/json'

    def __call__(self, fossil):
        return json.dumps(fossil, pretty=self.pretty)


Serializer.register('json', JSONSerializer)
