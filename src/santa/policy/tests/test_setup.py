# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from santa.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('santa.policy'))

    def test_actions__portal_tabs__index_html__visible(self):
        actions = getToolByName(self.portal, 'portal_actions')
        self.assertFalse(actions.portal_tabs.index_html.getProperty('visible'))

    def test_mailhost__smtp_host(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'smtp.gmail.com')

    def test_mailhost__smtp_port(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 587)

    def test_metadata__dependency__santa_theme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('santa.theme'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-santa.policy:default'),
            u'3')

    def test_portal_languages_supported_langs(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.assertEqual(languages.supported_langs, ['en', 'ja'])

    def test_properties__title(self):
        self.assertEqual(
            self.portal.getProperty('title'), 'SANTA ABITA')

    def test_properties__description(self):
        self.assertEqual(self.portal.getProperty('description'),
            'Santa Claus from Finland')

    def test_properties__email_from_address(self):
        self.assertEqual(
            self.portal.getProperty('email_from_address'), 'santa@abita.fi')

    def test_properties__email_from_name(self):
        self.assertEqual(
            self.portal.getProperty('email_from_name'), 'SANTA ABITA')

    def test_propertiestool_site_properties__default_language(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertEqual(site_properties.getProperty('default_language'), 'ja')

    def test_propertiestool_site_properties__disable_nonfolderish_sections(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertTrue(site_properties.getProperty('disable_nonfolderish_sections'))

    def test_propertiestool_site_properties__external_links_open_new_window(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertEqual(
            site_properties.getProperty('external_links_open_new_window'), 'true')

    def test_propertiestool_site_properties__use_email_as_login(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertTrue(site_properties.getProperty('use_email_as_login'))

    def test_propertiestool_site_properties__icon_visibility(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertEqual(
            site_properties.getProperty('icon_visibility'),
            'authenticated'
        )

    def test_propertiestool__webstats_js(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_props = properties.site_properties
        self.assertEqual(
            site_props.getProperty('webstats_js'),
            '<script type="text/javascript">\n\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-789306-1\']);\n_gaq.push([\'_setDomainName\', \'abita.fi\']);\n_gaq.push([\'_trackPageview\']);\n\n(function() {\nvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\nga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\nvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n\n</script>')

    def test_tinymce__autoresize(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.autoresize)

    def test_tinymce__link_using_uids(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.link_using_uids)

    def test_tinymce__toolbar_forecolor(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.toolbar_forecolor)

    def test_tinymce__toolbar_backcolor(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.toolbar_backcolor)

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.policy'])
        self.failIf(installer.isProductInstalled('santa.policy'))
