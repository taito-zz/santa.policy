from Products.CMFCore.utils import getToolByName
from plone.app.theming.interfaces import IThemeSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

package = 'santa.policy'


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


def create_objects(context, parent, ids, ctype='Folder', capitalize=True, language=''):
    logger = context.getLogger(package)
    if not isinstance(ids, list):
        ids = [ids]
    for oid in ids:
        if not parent.get(oid):
            title = oid.capitalize() if capitalize else oid
            obj = parent[
                parent.invokeFactory(
                    ctype,
                    oid,
                    title=title,
                    language=language,
                )
            ]
            obj.reindexObject()


def update_objects(context, parent, ids, language=''):
    logger = context.getLogger(package)
    if not isinstance(ids, list):
        ids = [ids]
    for oid in ids:
        obj = parent.get(oid)
        if obj:
            current_language = obj.Language()
            if current_language != language:
                message = 'Updating {0}.'.format(oid)
                logger.info(message)
                obj.getField('language').set(obj, language)
                obj.setTitle(oid.capitalize())
                obj.reindexObject()
                message = 'Updated {0}.'.format(oid)
                logger.info(message)


def update_folders_language(context):
    for oid in ['news', 'events']:
        portal = context.getSite()
        update_language(context, portal[oid])


def create_languages(context, parent):
    logger = context.getLogger(package)
    portal = context.getSite()
    languages = getToolByName(portal, 'portal_languages')
    pid = parent.id
    for oid in languages.supported_langs:
        obj = parent.get(oid)
        if not obj:
            message = 'Creating {0} in {1}.'.format(oid, pid)
            logger.info(message)
            obj = parent[
                parent.invokeFactory(
                    'Document',
                    oid,
                    language=oid,
                )
            ]
            obj.reindexObject()
            message = 'Created {0} in {1}.'.format(oid, pid)
            logger.info(message)


def exclude_from_nav(context, obj):
    logger = context.getLogger(package)
    if not obj.exclude_from_nav():
        oid = obj.id
        message = 'Excluding {0} from navivation.'.format(oid)
        logger.info(message)
        obj.setExcludeFromNav(True)
        obj.reindexObject(idxs=['exclude_from_nav'])
        message = 'Excluded {0} from navivation.'.format(oid)
        logger.info(message)


def setupVarious(context):

    if context.readDataFile('santa.policy_various.txt') is None:
        return

    uninstall_package(context, ['plonetheme.classic', 'santa.worldpolicy'])

    portal = context.getSite()
    update_objects(context, portal, ['news', 'events'])

    create_objects(context, portal, ['foundation', 'partners', 'cases', 'head'])
    for oid in ['cases', 'foundation', 'head', 'partners']:
        create_languages(context, portal[oid])
    exclude_from_nav(context, portal['head'])
