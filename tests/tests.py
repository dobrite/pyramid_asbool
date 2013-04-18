import unittest


class Test_asbool(unittest.TestCase):
    def _callFUT(self, s):
        from pyramid_asbool import asbool
        return asbool(s)

    def test_s_is_None(self):
        result = self._callFUT(None)
        self.assertEqual(result, False)

    def test_s_is_True(self):
        result = self._callFUT(True)
        self.assertEqual(result, True)

    def test_s_is_False(self):
        result = self._callFUT(False)
        self.assertEqual(result, False)

    def test_s_is_true(self):
        result = self._callFUT('True')
        self.assertEqual(result, True)

    def test_s_is_false(self):
        result = self._callFUT('False')
        self.assertEqual(result, False)

    def test_s_is_yes(self):
        result = self._callFUT('yes')
        self.assertEqual(result, True)

    def test_s_is_on(self):
        result = self._callFUT('on')
        self.assertEqual(result, True)

    def test_s_is_1(self):
        result = self._callFUT(1)
        self.assertEqual(result, True)

    def test_s_is_checkmark(self):
        checkmark = b'\xe2\x9c\x93'.decode('utf-8')

        result = self._callFUT(checkmark)
        self.assertEqual(result, True)

    def test_s_is_bold_checkmark(self):
        bold_check = b'\xe2\x9c\x94'.decode('utf-8')

        result = self._callFUT(bold_check)
        self.assertEqual(result, True)


class Test_patch_asbool(unittest.TestCase):
    def _callFUT(self):
        from pyramid_asbool import patch_asbool
        patch_asbool()

    def test_patch_asbool_checkmark(self):
        checkmark = b'\xe2\x9c\x93'.decode('utf-8')

        self._callFUT()
        from pyramid.settings import asbool

        result = asbool(checkmark)
        self.assertEqual(result, True)

    def test_patch_asbool_bold_checkmark(self):
        bold_check = b'\xe2\x9c\x94'.decode('utf-8')

        self._callFUT()
        from pyramid.settings import asbool

        result = asbool(bold_check)
        self.assertEqual(result, True)
