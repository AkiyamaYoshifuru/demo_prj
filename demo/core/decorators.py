from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from django.core.exceptions import PermissionDenied

'''
def validate_request_for_login(f):
    def wrap(request):
        # TypeError: 'bool' object is not callable
        if not request.user.is_authenticated():
            return redirect("/login?next=" + request.path)
        return f(request)
    return wrap
'''
# In Django 1.9+, you can use the UserPassesTestMixin instead of a decorator, and set raise_exception to True.
def officer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_officer,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def operator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_operator,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
