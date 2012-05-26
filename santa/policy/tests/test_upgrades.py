from Products.CMFCore.utils import getToolByName
from santa.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_upgrades_1_to_2(self):

        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        site_properties.manage_changeProperties(webstats_js='')
        self.failIf(site_properties.getProperty('webstats_js'))

        from santa.policy.upgrades import upgrade_1_to_2
        upgrade_1_to_2(self.portal)

        self.assertEqual(
            site_properties.getProperty('webstats_js'),
            '<script type="text/javascript">\n\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-31909586-1\']);\n_gaq.push([\'_trackPageview\']);\n\n(function() {\nvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\nga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\nvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n\n</script>'
        )

    def test_upgrades_2_to_3(self):

        languages = getToolByName(self.portal, 'portal_languages')
        langs = ['en', 'fi', 'ja', 'zh']
        languages.supported_langs = langs
        self.assertEqual(
            languages.supported_langs,
            langs
        )

        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        site_properties.manage_changeProperties(default_editor=None, external_links_open_new_window='false')
        self.failIf(site_properties.getProperty('default_editor'))
        self.assertEqual(
                site_properties.getProperty('external_links_open_new_window'),
                'false'
        )

        from santa.policy.upgrades import upgrade_2_to_3
        upgrade_2_to_3(self.portal)

        self.assertEqual(
            languages.supported_langs,
            ['en', 'fi', 'ja']
        )

        self.assertEqual(
                site_properties.getProperty('external_links_open_new_window'),
                'true'
        )
