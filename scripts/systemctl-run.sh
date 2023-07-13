#!/bin/bash

set -eu

declare -r COMMAND="$1"

for i in 1 2 3
do
    systemctl ${COMMAND} monochat-server-${i}.service
done

