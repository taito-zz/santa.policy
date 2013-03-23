from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-santa.policy:default'


def reimport_actions(context):
    """Reimport actions"""
    reimport_profile(context, PROFILE_ID, 'actions')
