from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-santa.policy:default'


def upgrade_1_to_2(context, logger=None):
    """Reimport propertiestool.xml for webstats_js."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    logger.info('Reimporting propertiestool.xml.')
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        PROFILE_ID,
        'propertiestool',
        run_dependencies=False,
        purge_old=False,
    )
    logger.info('Reimported propertiestool.xml.')