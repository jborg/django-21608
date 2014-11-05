Django ticket 21608 test case

https://code.djangoproject.com/ticket/21608

Steps to reproduce:
1. python manage.py migrate
2. python manage.py createsuperuser
3. python manage.py runserver

4. Open http://localhost:8000/admin/ in tab 1 and login.
5. Open http://localhost:8000/slow/ in tab 2.
6. Before the slow page loads (takes 10 seconds) complete the following
   steps:
6.1. Logout from tab 1: http://localhost:8000/admin/logout/
6.2. Verify that http://localhost:8000/admin/ shows login form
6.3. Wait 10 seconds
6.4. Observe that http://localhost:8000/admin/ is logged in again.

