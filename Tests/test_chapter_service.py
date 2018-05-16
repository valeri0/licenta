from unittest import *

from Business.Services.ChapterService import ChapterService


class ChapterServiceTest(TestCase):

    def setUp(self):
        self.chapter_service = ChapterService()

    def tearDown(self):
        self.chapter_service = None

    def test_get_all_chapters(self):

        chapters = self.chapter_service.get_all_chapters()

        self.assertIsNotNone(chapters)
