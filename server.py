#!/usr/bin/env python3

import os
import json
import sys

from flask import Flask, render_template, redirect, request, make_response

STATIC_PATH = "/static"
STATIC_FOLDER = "static"
TEMPLATE_FOLDER = "templates"

app = Flask(__name__,
            static_url_path = STATIC_PATH,
            static_folder = STATIC_FOLDER,
            template_folder = TEMPLATE_FOLDER)

@app.route('/')
def index():
    return render_template("/index.html")
