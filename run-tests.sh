#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Mirek Šimek, VŠCHT Praha.
#
# oarepo-whitenoise is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

pydocstyle oarepo_whitenoise tests && \
isort -c oarepo_whitenoise && \
check-manifest --ignore ".travis-*" && \
pytest
