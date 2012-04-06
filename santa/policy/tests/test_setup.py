from santa.policy.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_santa_policy_installed(self):
        self.failUnless(self.installer.isProductInstalled('santa.policy'))

    def test_properties__title(self):
        self.assertEqual(
            self.portal.getProperty('title'),
            'Santa Claus Foundation Finland'
        )

    def test_properties__email_from_address(self):
        self.assertEqual(
            self.portal.getProperty('email_from_address'),
            'santa@abita.fi'
        )

    def test_properties__email_from_name(self):
        self.assertEqual(
            self.portal.getProperty('email_from_name'),
            'Santa Claus Foundation Finland'
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

    # def test_theme__enabled(self):
    #     from zope.component import getUtility
    #     from plone.registry.interfaces import IRegistry
    #     registry = getUtility(IRegistry)
    #     from plone.app.theming.interfaces import IThemeSettings
    #     settings = registry.forInterface(IThemeSettings)
    #     self.assertTrue(settings.enabled)

    # def test_theme__rules(self):
    #     from zope.component import getUtility
    #     from plone.registry.interfaces import IRegistry
    #     registry = getUtility(IRegistry)
    #     from plone.app.theming.interfaces import IThemeSettings
    #     settings = registry.forInterface(IThemeSettings)
    #     self.assertEqual(
    #         settings.rules,
    #         "/++theme++santa.theme/rules.xml"
    #     )

    # def test_theme__absolutePrefix(self):
    #     from zope.component import getUtility
    #     from plone.registry.interfaces import IRegistry
    #     registry = getUtility(IRegistry)
    #     from plone.app.theming.interfaces import IThemeSettings
    #     settings = registry.forInterface(IThemeSettings)
    #     self.assertEqual(
    #         settings.absolutePrefix,
    #         "/++theme++santa.theme"
    #     )

    def test_uninstall(self):
        self.installer.uninstallProducts(['santa.policy'])
        self.failIf(self.installer.isProductInstalled('santa.policy'))
