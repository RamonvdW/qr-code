#!/bin/bash

#  Copyright (c) 2019-2025 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

# ga naar de directory waar het script staat
cd $(dirname $0)

for req in requirements
do
    OUT="$req.txt"
    IN="$req.in"
    echo "[INFO] Creating $OUT"
    [ -f "$OUT" ] && rm "$OUT"
    pip-compile --resolver=backtracking --strip-extras -q "$IN"
done

echo
echo "Press enter to pip-sync dev, ^C to abort"
read

echo "[INFO] Running pip-sync requirements.txt"
pip-sync requirements.txt

# end of file

