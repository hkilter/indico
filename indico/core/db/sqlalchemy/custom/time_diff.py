# This file is part of Indico.
# Copyright (C) 2002 - 2017 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from sqlalchemy import types
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.functions import FunctionElement


class time_diff(FunctionElement):
    name = 'time_diff'
    type = types.Numeric


@compiles(time_diff, 'default')
def _time_diff_default(element, compiler, **kw):
    arg1, arg2 = list(element.clauses)
    return '{} - {}'.format(arg2, arg1)


@compiles(time_diff, 'postgresql')
def _time_diff_postgres(element, compiler, **kw):
    arg1, arg2 = list(element.clauses)
    return 'EXTRACT(epoch FROM {}::time) - EXTRACT(epoch FROM {}::time)'.format(arg2, arg1)