from Products.CMFCore.utils import getToolByName

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


def update_objects(context, parent, oids, language=''):
    logger = context.getLogger(package)
    if not isinstance(oids, list):
        oids = [oids]
    for oid in oids:
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
            obj.setExcludeFromNav(True)
            obj.reindexObject()
            message = 'Created {0} in {1}.'.format(oid, pid)
            logger.info(message)


def setPortalView(context):
    portal = context.getSite()
    if portal.getLayout() != 'santa-view':
        logger = context.getLogger(package)
        logger.info('Setting portal laytout to santa-view.')
        portal.setLayout('santa-view')
        logger.info('Set portal laytout to santa-view.')


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


def removeFolders(context, oids):
    portal = context.getSite()
    if not isinstance(oids, list):
        oids = [oids]
    oids = [oid for oid in oids if portal.get(oid)]
    logger = context.getLogger(package)
    message = 'Removing {0}.'.format(', '.join(oids))
    logger.info(message)
    portal.manage_delObjects(oids)
    message = 'Removed {0}.'.format(', '.join(oids))
    logger.info(message)


def updateCases(context):
    portal = context.getSite()
    oid = 'cases'
    item = portal[oid]
    title = 'Use Cases'
    if item.Title() != title:
        logger = context.getLogger(package)
        message = 'Setting {0} title to {1}.'.format(oid, title)
        logger.info(message)
        item.setTitle(title)
        item.reindexObject(idxs=['Title'])
        message = 'Set {0} title to {1}.'.format(oid, title)
        logger.info(message)


def setupVarious(context):

    if context.readDataFile('santa.policy_various.txt') is None:
        return

    uninstall_package(context, ['plonetheme.classic', 'santa.worldpolicy', 'santa.worldtheme'])

    portal = context.getSite()

    create_objects(context, portal, ['foundation', 'partners', 'cases', 'inquiries'])

    update_objects(context, portal, ['news', 'events', 'partners', 'links', ])

    for oid in ['cases', 'foundation', 'partners', 'inquiries']:
        create_languages(context, portal[oid])

    setPortalView(context)
    removeFolders(context, ['Members', 'products', 'about'])

    updateCases(context)
