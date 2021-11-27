
import unittest
import schema
import sprout

from schema import Schema, And, Use, Optional, SchemaError


class TestContextMerging(unittest.TestCase):
    def setUp(self):
        sprout.ctx.reset_context()
        sprout.ctx.set_base()

    def test_schema(self):
        sprout.ctx.get_sprout('default').validate()

    def test_basic_api(self):
        sprout.add_sources('test.c')
        self.assertTrue(
            sprout.ctx.get_sprout('default').contains_source('test.c')
        )

        sprout.add_defines('TEST')
        self.assertTrue(
            sprout.ctx.get_sprout('default').contains_define('TEST')
        )

        sprout.add_includes('test')
        self.assertTrue(
            sprout.ctx.get_sprout('default').contains_include('test')
        )

        sprout.ctx.reset_context()
        self.assertFalse(
            sprout.ctx.get_sprout('default').contains_source('test.c')
        )

    def test_merge_append(self):
        self.assertFalse(
            sprout.ctx.get_sprout('default').contains_source('test.c')
        )

        sprout.add_sources('test.c')
        sprout.add_sources('hello.c')
        self.assertTrue(
            sprout.ctx.get_sprout('default').contains_source('test.c')
        )
        self.assertTrue(
            sprout.ctx.get_sprout('default').contains_source('hello.c')
        )
