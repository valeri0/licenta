from Data.Domain.Chapter import ChapterLesson,Chapter,ChapterExercise
from Data.Persistance.database import db_session

class ChapterRepository:
    db_context = db_session

    def get_all_chapters(self):
        return Chapter.query.all()
