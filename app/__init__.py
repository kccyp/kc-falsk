from flask import Flask
import os
import sys


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    print(template_folder,static_folder)
    test_app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    test_app = Flask(__name__)


from app import route