from time import sleep
from django.http import HttpResponse


def slow(request):
    assert request.user.is_authenticated()
    # Sleep for a while to make it possible to logout the session
    # in a separate tab before this request completes
    sleep(10)
    # Make session dirty
    request.session['x'] = 42
    return HttpResponse('Nap over')

