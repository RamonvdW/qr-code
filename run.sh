#!/bin/bash

#  Copyright (c) 2022 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

export PYTHONDONTWRITEBYTECODE=1

./manage.py check
[ $? -eq 0 ] || exit 1

# start the development webserver
echo "[INFO] Starting runserver"
./manage.py runserver

# end of file
