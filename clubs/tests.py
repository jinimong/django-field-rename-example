from django.test import TestCase
from .models import Club


class ModelTest(TestCase):
    def test_club_members_m2m_field_table(self):
        self.assertEqual(Club.members.through._meta.db_table, "clubs_club_members")
