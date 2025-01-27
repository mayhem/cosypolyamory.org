#!/usr/bin/env python3

import os
import json
import sys

from flask import Flask, render_template, send_file

STATIC_PATH = "/static"
STATIC_FOLDER = "static"
TEMPLATE_FOLDER = "templates"

app = Flask(__name__,
            static_url_path = STATIC_PATH,
            static_folder = STATIC_FOLDER,
            template_folder = TEMPLATE_FOLDER)

@app.route('/robots.txt')
@app.route('/sitemap.xml')

@app.route('/')
def index():
    return render_template("/index.html", page="home")

@app.route('/contact')
def contact():
    return render_template("/contact.html", page="contact")

@app.route('/values')
def values():
    return render_template("/values.html", page="values")

@app.route('/structure')
def rules():
    return render_template("/structure.html", page="docs")

@app.route('/governance')
def governance():
    return render_template("/governance.html", page="docs")

@app.route('/conflict-resolution')
def conflict():
    return send_file("static/pdf/Cosy Polyamory Community - Conflict Resolution Protocol.pdf")

@app.route('/code-of-conduct')
def coc():
    return send_file("static/pdf/Cosy Polyamory Community - Code of Conduct.pdf")
