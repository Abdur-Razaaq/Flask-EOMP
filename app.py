import hmac
import sqlite3

from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS


class User(object)
    def __init__(self, phone, email, password):
        self.phone = phone
        self.email = email
        self.password = password