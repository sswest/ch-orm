import unittest

from clickhouse_orm.database import Database, ServerError
from clickhouse_orm.engines import MergeTree
from clickhouse_orm.fields import UUIDField, DateField
from clickhouse_orm.models import TemporaryTable
from clickhouse_orm.session import in_session


class TemporaryTest(unittest.TestCase):

    def setUp(self):
        self.database = Database('test-db', log_statements=True)

    def tearDown(self):
        self.database.drop_database()

    def test_create_table(self):
        with self.assertRaises(ServerError):
            self.database.create_table(Temporary1)
        with self.assertRaises(AssertionError):
            self.database.create_table(Temporary2)
        with in_session():
            self.database.create_table(Temporary1)
            count = Temporary1.objects_in(self.database).count()
            self.assertEqual(count, 0)
        # Check if temporary table is cleaned up
        with self.assertRaises(ServerError):
            Temporary1.objects_in(self.database).count()


class Temporary1(TemporaryTable):
    date_field = DateField()
    uuid = UUIDField()


class Temporary2(TemporaryTable):
    date_field = DateField()
    uuid = UUIDField()

    engine = MergeTree('date_field', ('date_field',))
