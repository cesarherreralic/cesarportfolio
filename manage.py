#!/usr/bin/env python2.7
from django.core import management
import imp
import os
import sys

#try:
#    imp.find_module('settings') # Assumed to be in the same directory.
#except ImportError:
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
#    sys.exit(1)

#import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    management.execute_from_command_line(sys.argv)

#import settings

#if __name__ == "__main__":
#    execute_manager(settings)
