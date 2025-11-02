from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView,expose


class User(UserMixin):

    def __init__(self, id):
        self.id = id


class NewsView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'


class BlogView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    edit_template = 'admin/edit.html'
    create_template = 'admin/create.html'


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    #edit_template = 'admin/edit.html'
    #create_template = 'admin/create.html'
    base_template="admin/clayout.html"
