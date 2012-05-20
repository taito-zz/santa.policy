from Products.CMFCore.utils import getToolByName
from santa.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_santa_policy_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.policy'))

    def test_santa_theme_istalled(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.theme'))

    def test_PloneFormGen_istalled(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PloneFormGen'))

    def test_LinguaPlone_istalled(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('LinguaPlone'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-santa.policy:default'),
            u'2'
        )

    def test_portal_languages_use_cookie_negotiation(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.assertTrue(languages.use_cookie_negotiation)

    def test_portal_languages_use_request_negotiation(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.assertTrue(languages.use_request_negotiation)

    def test_portal_languages_supported_langs(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.assertEqual(
            languages.supported_langs,
            ['en', 'fi', 'ja', 'zh']
        )

    def test_portlets_Login(self):
        from plone.portlets.interfaces import IPortletType
        from zope.component import queryUtility
        portlet = queryUtility(IPortletType, name='portlets.Login')
        self.failIf(portlet)

    def test_portlets_Classic(self):
        from plone.portlets.interfaces import IPortletType
        from zope.component import queryUtility
        portlet = queryUtility(IPortletType, name='portlets.Classic')
        self.failIf(portlet)

    def test_portlets__news_removed_from_right_column(self):
        from zope.component import getMultiAdapter
        from zope.component import getUtility
        from plone.portlets.interfaces import IPortletManager
        from plone.portlets.interfaces import IPortletAssignmentMapping
        column = getUtility(IPortletManager, name=u"plone.rightcolumn")
        assignable = getMultiAdapter((self.portal, column), IPortletAssignmentMapping)
        self.assertFalse('news' in assignable.keys())

    def test_portlets__events_removed_from_right_column(self):
        from zope.component import getMultiAdapter
        from zope.component import getUtility
        from plone.portlets.interfaces import IPortletManager
        from plone.portlets.interfaces import IPortletAssignmentMapping
        column = getUtility(IPortletManager, name=u"plone.rightcolumn")
        assignable = getMultiAdapter((self.portal, column), IPortletAssignmentMapping)
        self.assertFalse('events' in assignable.keys())

    def test_properties__title(self):
        self.assertEqual(
            self.portal.getProperty('title'),
            'Santa Claus Foundation'
        )

    def test_properties__email_from_address(self):
        self.assertEqual(
            self.portal.getProperty('email_from_address'),
            'santa@abita.fi'
        )

    def test_properties__email_from_name(self):
        self.assertEqual(
            self.portal.getProperty('email_from_name'),
            'Santa Claus Foundation'
        )

    def test_properties__default_page(self):
        self.assertEqual(
            self.portal.getProperty('default_page'),
            'sll-view'
        )

    def test_propertiestool_site_properties__default_language(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertEqual(
            site_properties.getProperty('default_language'),
            'en'
        )

    def test_propertiestool_site_properties__disable_nonfolderish_sections(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertTrue(site_properties.getProperty('disable_nonfolderish_sections'))

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

    def test_propertiestool_site_properties__exposeDCMetaTags(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertTrue(site_properties.getProperty('exposeDCMetaTags'))

    def test_propertiestool_site_properties__enable_sitemap(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertTrue(site_properties.getProperty('enable_sitemap'))

    def test_propertiestool__webstats_js(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_props = properties.site_properties
        self.assertEqual(
            site_props.getProperty('webstats_js'),
            '<script type="text/javascript">\n\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-31909586-1\']);\n_gaq.push([\'_trackPageview\']);\n\n(function() {\nvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\nga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\nvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n\n</script>'
        )

    def test_mailhost__smtp_host(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'smtp.nebula.fi')

    def test_mailhost__smtp_port(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 25)

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

    def test_jsregistry__kukit(self):
        javascripts = getToolByName(self.portal, 'portal_javascripts')
        self.assertFalse(javascripts.getResource("++resource++kukit.js").getAuthenticated())

    def test_folder__news__language(self):
        item = self.portal['news']
        self.assertEqual(item.Language(), '')

    def test_folder__news__title(self):
        item = self.portal['news']
        self.assertEqual(item.Title(), 'News')

    def test_folder__events__language(self):
        item = self.portal['events']
        self.assertEqual(item.Language(), '')

    def test_folder__events__title(self):
        item = self.portal['events']
        self.assertEqual(item.Title(), 'Events')

    def test_folder__head(self):
        languages = getToolByName(self.portal, 'portal_languages')
        for lang in languages.supported_langs:
            self.failUnless(self.portal['foundation'][lang])

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.policy'])
        self.failIf(installer.isProductInstalled('santa.policy'))
