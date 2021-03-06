#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by OCraig
# Copyright (c) 2015 OCraig
#
# License: MIT
#

"""This module exports the Lessc plugin class."""

from SublimeLinter.lint import Linter, util


class Lessc(Linter):

    """Provides an interface to lessc."""

    syntax = ''
    cmd = 'lessc'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r''
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

