""" Test custom Django manegment commands.

"""
from  unittest.mock import patch 
from django.core.management import call_command

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError 
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')

class CommandTests(SimpleTestCase):
  """ Test commands."""

  def test_wait_for_db_ready(self,patch_check):
      """Test waiting for db when db is available."""
      patch_check.return_value = True 
      call_command('wait_for_db')
      patch_check.assert_called_once_with(databse=['default'])

  @patch('time.sleep')
  def test_wait_for_db_delay(self,patched_sleep, patched_check):
        """Test waiting for db when db is delayed."""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assert_called_with(database=['default'])
        patched_check.assert_called_with(database=['default'])