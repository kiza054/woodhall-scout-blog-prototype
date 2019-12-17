import flask_login as login
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request, flash

class AdminView(ModelView):
    can_export = True
    page_size = 50
    column_exclude_list = ['password_hash']
    column_searchable_list = ['username', 'email', 'leader']
    column_editable_list = ['is_admin', 'about_me', 'childs_section', 'leader']
    create_modal = True
    edit_modal = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        return login.current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            flash('403: Sorry, you don\'t have access to this page.')
            return redirect(url_for('index'))