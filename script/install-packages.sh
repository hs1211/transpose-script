#!/bin/bash

set -e


function create_venv() {
    mkdir -p ./venv
}

function install_dependencies(){
    PIPENV_VENV_IN_PROJECT=true pipenv install
}


create_venv
install_dependencies