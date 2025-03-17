from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView


class User(UserMixin):

    def __init__(self, id):
        self.id = id


class NewsView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class BlogView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    form_ajax_refs = {
        'news': {
            'fields': ['name', 'description'],
            'page_size': 10
        }
    }
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
