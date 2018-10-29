# Multi user Blog Approval Application

There are three type of user how can use this application, Editor, Chief and anonymous. Anonymous can read only those blogs which is approved by chief.

    - Editor: Can create and read blogs.
    - Chief: Can read, write, and approve editors blog.
    - Anonymous: Only read approved blogs.

### Quick Setup
- Create a vitual environment.
  - `virtualenv -p python3.6 venv`
- Activate your virtual environment by
  - `source venv/bin/activate`
- Install required python libraries by using `pip`.
  - `pip install -r requirements.txt`
- Migrate database queries.
  - `python manage.py migrate`
- Finally, run your django runserver.
  - `python manage.py runserver`