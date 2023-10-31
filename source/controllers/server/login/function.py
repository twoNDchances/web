from flask import render_template, session, request, redirect, url_for, flash
from flask_login import login_user
from source.controllers.server.login.form import LoginForm
from source.controllers.processors.queries import check_password, query_object_user_by_username


def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        get_username = form.username.data
        get_password = form.password.data
        get_user = query_object_user_by_username(username=get_username)
        if get_user is not None and check_password(username=get_username, password=get_password):
            session['username'] = get_user.username
            login_user(get_user)
            do_next = request.args.get('next')
            if do_next is None:
                return redirect(url_for('server.home.main_root_page_'))
            else:
                return redirect(do_next)
        else:
            flash('Your account maybe incorrect or not exist!')
    return render_template(template_name_or_list='login_page.html', form=form)

