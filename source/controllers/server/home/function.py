from flask import render_template, redirect, url_for

def main_root():
    return redirect(url_for('server.home._home_page_'))

def home_page():
    return render_template(template_name_or_list='home_page.html')
