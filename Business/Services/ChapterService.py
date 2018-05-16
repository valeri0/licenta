from Business.Repositories.ChapterRepository import ChapterRepository

class ChapterService:

    _chapter_repository = ChapterRepository()

    def get_all_chapters(self):
        return self._chapter_repository.get_all_chapters()