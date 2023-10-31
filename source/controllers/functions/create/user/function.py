from source.controllers.functions.create.user.form import RegisterForm
from source import database
from source.datatable import User
from flask import render_template, redirect, url_for
from source.controllers.processors.queries import _query_object_user_by_username


def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        get_username = form.username.data
        get_password = form.cf_pword.data
        is_empty = _query_object_user_by_username(username=get_username)
        if is_empty is None:
            new_user = User(username=get_username, password=get_password)
            database.session.add(new_user)
            database.session.commit()
            return redirect(url_for('server.login._login_page_'))
        return render_template(template_name_or_list='register_page.html', not_empty=True, form=form)
    return render_template(template_name_or_list='register_page.html', form=form)
