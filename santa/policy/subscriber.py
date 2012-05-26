from Products.CMFCore.utils import getToolByName
from five import grok
from santa.content.partner import IPartner
from zope.lifecycleevent.interfaces import IObjectAddedEvent


@grok.subscribe(IPartner, IObjectAddedEvent)
def add_documents(context, event):
    """Add documents for each languages."""
    languages = getToolByName(context, 'portal_languages')
    for oid in languages.supported_langs:
        obj = context.get(oid)
        if not obj:
            obj = context[
                context.invokeFactory(
                    'Document',
                    oid,
                    language=oid,
                )
            ]
            obj.setExcludeFromNav(True)
            obj.reindexObject()
