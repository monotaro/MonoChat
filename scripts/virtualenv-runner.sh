#!/bin/bash

set -eu

declare -r ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
declare -r VIRTUALENV_DIR="${ROOT_DIR}/.venv"

export PYTHONPATH="${ROOT_DIR}/monochat_beta"
export PYTHONPYCACHEPREFIX="${ROOT_DIR}/target/__pycache__"

declare -r EXIT_STATUS_SUCCESS=0
declare -r EXIT_STATUS_INVALID_ARGUMENTS=1

function main
{
    declare -r COMMAND="$@"

    case "${COMMAND}" in
        setup | repl | run | test | coverage)
            command:${COMMAND}
            exit ${EXIT_STATUS_SUCCESS}
            ;;
        *)
            echo -e "invalid arguments: [${COMMAND}]" >&2
            exit ${EXIT_STATUS_INVALID_ARGUMENTS}
            ;;
    esac
}

function command:setup
{
    if [[ -d "${VIRTUALENV_DIR}" ]]; then
        echo "SKIP: virtualenv environment already exists."
    else
        virtualenv --python=python3 "${VIRTUALENV_DIR}"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    pip install -r requirements.txt
}

function command:repl
{
    source "${VIRTUALENV_DIR}/bin/activate"
    python
}

function command:run
{
    if [[ -f "${ROOT_DIR}/credentials/export-credentials.sh" ]]; then
        source "${ROOT_DIR}/credentials/export-credentials.sh"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    python "${ROOT_DIR}/monochat_beta/main.py"
}

function command:test
{
    if [[ -f "${ROOT_DIR}/credentials/export-credentials.sh" ]]; then
        source "${ROOT_DIR}/credentials/export-credentials.sh"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    python -m unittest discover -t "${ROOT_DIR}" -s "${ROOT_DIR}/tests"
}

function command:coverage
{
    if [[ -f "${ROOT_DIR}/credentials/export-credentials.sh" ]]; then
        source "${ROOT_DIR}/credentials/export-credentials.sh"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    export COVERAGE_FILE="${ROOT_DIR}/target/coverage"
    coverage erase
    coverage run --branch --omit 'tests/*' -m unittest discover -t "${ROOT_DIR}" -s "${ROOT_DIR}/tests"
    coverage report
    coverage html --directory=./target/docs/coverage/
}

main "$@"

