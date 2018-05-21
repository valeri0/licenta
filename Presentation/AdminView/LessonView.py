from flask_admin.contrib.sqla import ModelView

class LessonView(ModelView):
    column_display_pk = True
    form_columns = ['title','content','instructions','source_code']
    column_list = form_columns + ['id']