from __future__ import absolute_import, division, print_function
import sys

PY3 = sys.version_info[0] >= 3
if PY3:
    raw_input = input
    xrange = range
    integer_types = (int,)
    string_types = (str,)
    text_type = str
    def execfile(fname, globs, locs=None):
        exec(compile(open(fname).read(), fname, 'exec'), globs, locs or globs)
else:
    raw_input = raw_input
    xrange = xrange
    integer_types = (int, long)
    string_types = (basestring,)
    text_type = unicode
    execfile = execfile
