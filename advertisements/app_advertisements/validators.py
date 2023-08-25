from django.core.exceptions import ValidationError

def validate_question_mark(value):
    """Если сообщение начинается с '?' то выводится ошибка"""
    if value.startswith('?'):
        msg = 'Заголовок не может начинаться в восклицательного знака'
        raise ValidationError(msg)