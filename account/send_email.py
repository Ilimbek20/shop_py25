

from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'Братан для регистрации перейди по сссылке ---> http://localhost:8000/api/v1/account/activate/{code}', # body
        'ajnarg523@gmail.com', # from
        [email] # to
    )


def send_reset_password_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'Приветсвую уважаемый! Чтобы сбросить пароль, тебе нужен этот код = {code}', # body
        'ajnarg523@gmail.com', # from
        [email] # to
    )