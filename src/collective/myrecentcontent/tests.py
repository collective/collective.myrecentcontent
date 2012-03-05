import doctest

from plone.testing import layered

from collective.myrecentcontent import testing

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE |
               doctest.REPORT_NDIFF)


def test_suite():
    return layered(
        doctest.DocFileSuite('tests.txt', optionflags=optionflags),
        layer=testing.MY_RECENT_FUNCTIONAL_TESTING)
