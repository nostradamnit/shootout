import web
from web import form

bookmark_form = form.Form(
    form.Textbox('url'),
    form.Textarea('description'),
    form.Checkbox('public')
)

registration_form = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Password('confirm password'),
    form.Textbox('email'),
    form.Textbox('confirm email')
)

login_form = form.Form(
    form.Textbox('username'),
    form.Password('password')
)
