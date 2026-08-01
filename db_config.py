"""Central database configuration for the Hotel Management System.

Credentials are read from config.ini (kept out of git) and may be overridden by
environment variables, so no password is ever hardcoded in the source files.
"""

import configparser
import os

import mysql.connector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.ini")

_DEFAULTS = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "bank_management",
}


def _load_settings():
    settings = dict(_DEFAULTS)

    parser = configparser.ConfigParser()
    if parser.read(CONFIG_PATH) and parser.has_section("mysql"):
        for key in settings:
            if parser.has_option("mysql", key):
                settings[key] = parser.get("mysql", key)

    # Environment always wins, so deployments never need to ship a config file.
    for key in settings:
        env_value = os.environ.get("HOTEL_DB_" + key.upper())
        if env_value is not None:
            settings[key] = env_value

    return settings


def get_connection():
    """Open a new connection to the hotel database."""
    settings = _load_settings()
    return mysql.connector.connect(
        host=settings["host"],
        user=settings["user"],
        password=settings["password"],
        database=settings["database"],
    )
