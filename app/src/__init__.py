import os
from functools import wraps
from re import A

import jwt
from flask import Flask, jsonify, request

import src
from src.infrastructure.controllers import api
from src.infrastructure.Dependencies import Dependencies

app = Flask(__name__)

# init Dependencies to Injection
dependencies = Dependencies()
dependencies.init_resources()
dependencies.wire(packages=[src])

app.container = dependencies

# Init api namespaces
api.init_app(app)
