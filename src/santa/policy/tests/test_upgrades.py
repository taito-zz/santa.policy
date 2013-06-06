from santa.policy.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade step"""

    def test_reimport_actions(self):
        from santa.policy.upgrades import reimport_actions
        setup = mock.Mock()
        reimport_actions(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-santa.policy:default', 'actions', run_dependencies=False, purge_old=False)
