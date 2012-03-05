from zope.configuration import xmlconfig

from plone.testing import z2
from plone.app import testing

from Acquisition import aq_parent

from plone.app.toolbar import testing as toolbar


class MyRecentLayer(testing.PloneSandboxLayer):

    defaultBases = (toolbar.TOOLBAR_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.myrecentcontent
        xmlconfig.file('configure.zcml',
                       collective.myrecentcontent,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        z2.login(aq_parent(portal)['acl_users'],
                 testing.SITE_OWNER_NAME)
        portal.invokeFactory(type_name='Document', id='front-page')


MY_RECENT_FIXTURE = MyRecentLayer()
MY_RECENT_FUNCTIONAL_TESTING = testing.FunctionalTesting(
    bases=(MY_RECENT_FIXTURE,),
    name="MyRecentLayer:Functional")
