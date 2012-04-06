from Products.CMFCore.utils import getToolByName
from plone.app.theming.interfaces import IThemeSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


def setUpDoctype(portal):
    settings = getUtility(IRegistry).forInterface(IThemeSettings, False)
    settings.doctype = '<!DOCTYPE html>'


def uninstall_package(context, packages):
    """Uninstall packages.

    :param packages: List of package names.
    :type packages: list
    """
    portal = context.getSite()
    installer = getToolByName(portal, 'portal_quickinstaller')
    packages = [
        package for package in packages if installer.isProductInstalled(
            package
        )
    ]
    installer.uninstallProducts(packages)


def setupVarious(context):

    if context.readDataFile('santa.policy_various.txt') is None:
        return

    # portal = context.getSite()
    # setUpDoctype(portal)
    uninstall_package(context, ['santa.worldpolicy'])
