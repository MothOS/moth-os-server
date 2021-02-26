# -*- coding: utf-8 -*-
import os
from moth_os import __version__
from moth_os import api

API_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config/moth_os.yaml")

if __name__ == "__main__":
    print(f"MothOS {__version__}")
    api.init(API_CONFIG_FILE)
