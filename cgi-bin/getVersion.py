#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    version = utils.get_selected_version()
    response["server-version"] = version
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getVersion.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
