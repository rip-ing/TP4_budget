import os
os.system('git bisect start ba5d31c e4cfc6f')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
