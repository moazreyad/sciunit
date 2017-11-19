from __future__ import absolute_import

from nose.tools import *

import testit


class TestGiven(testit.LocalCase):
    def test_cli(self):
        with assert_raises(SystemExit) as r:
            testit.sciunit('given')
        assert_equals(r.exception.code, 2)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', '-i', 'repeat', 'e1')
        assert_equals(r.exception.code, 2)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', '*', 'repeat', '-x')
        assert_equals(r.exception.code, 2)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', '*', 'commit', 'e1')
        assert_equals(r.exception.code, 2)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', '*-', 'repeat', 'e1')  # no match
        assert_equals(r.exception.code, 1)

    def test_all(self):
        testit.sciunit('create', 'ok')
        testit.touch('tmp/file1')
        testit.touch('tmp/file2')
        testit.touch('tmp/d/file3')
        testit.touch('tmp/d2/file4')
        testit.sciunit('exec', 'cat', 'tmp/file1')

        with assert_raises(SystemExit) as r:
            testit.sciunit('repeat', 'e1', 'tmp/file2')
        assert_equals(r.exception.code, 1)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', 'tmp/file?', 'repeat', 'e1', 'tmp/file2')
        assert_equals(r.exception.code, 0)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', 'tmp/*/file?', 'repeat', 'e1', '%')
        assert_equals(r.exception.code, 0)

        testit.sciunit('commit')

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', 'tmp/*/file?', 'repeat', 'e1', '%', '%')
        assert_equals(r.exception.code, 1)

        with assert_raises(SystemExit) as r:
            testit.sciunit('given', 'tmp/file2',
                           'repeat', 'e2', 'tmp/d/file3', '%')
        assert_equals(r.exception.code, 0)