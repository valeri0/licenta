from unittest import *

from Business.Services.LessonService import LessonService


class LessonServiceTest(TestCase):

    def setUp(self):
        self.lesson_service = LessonService()

    def tearDown(self):
        self.lesson_service = None

    def test_get_lessons_ordered_by_id(self):

        lessons = self.lesson_service.get_lessons_ordered_by_id()
        self.assertTrue(len(lessons) != 0)
