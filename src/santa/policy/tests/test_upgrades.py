from santa.policy.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade step"""

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('santa.policy.upgrades.reimport_profile')
    def test_reimport_actions(self, reimport_profile):
        from santa.policy.upgrades import reimport_actions
        reimport_actions(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-santa.policy:default', 'actions')
