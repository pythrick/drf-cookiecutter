#!/bin/bash

# Default values of arguments:
# The container can run as the api, worker or scheduler. This arguments are mutually exclusive:
# Api server in dev mode on/off
DEVELOPMENT=0
# Worker on/off
RQW=0
# Scheduler on/off
RQS=0
################################################################################################
# Schedule tasks on start on/off
RQT=0
# Start the server without loading fixtures, default is to load (= 0)
NO_FIXTURES=0
# PATH TO LOAD FIXTURES FROM
FIXTURES_PATH='fixtures/development/*.json'
# Wipe database before running migrations, defaults to no. (=0)
WIPE=0
# New Relic on/off
NEW_RELIC=0
# New Relic Environment
NEW_RELIC_ENVIRONMENT='development'
# Server bind address and port
S_ADDRESS='0.0.0.0'
PORT='8000'


display_help() {
    echo "Usage: $0 [option...] {n|p|a,nre}" >&2
    echo
    echo "   -h, --help                 Show this help message and exit"
    echo "   -d, --development          Set the application server to run as run-server dev mode"
    echo "   -n, --newrelic             Start with NewRelic"
    echo "   -nf, --no-fixtures         Start the server without fixtures"
    echo "   -pf, --production-fixtures Set fixtures load path to fixtures/production/*.json instead of fixtures/development/*.json"
    echo "   -w, --worker               Start the server as rq-worker node"
    echo "   -s, --scheduler            Start the server as rq-scheduler node"
    echo "   -t, --tasks                Schedule tasks in rq-scheduler node"
    echo "   -nre=, --nrenv=            Set New Relic Environment {development|test|staging|production}, default=development"
    echo "   -p=, --port=               Set server starting port, default=8000"
    echo "   -a=, --address=            Set server listening address, default=0.0.0.0"
    echo "   -w=, --wipe=               Wipe the DB before running migrations."
    echo
    exit 0
}

exit_with_error(){
    echo "Something went wrong"
    exit 1
}

start_server_with_newrelic(){
    echo "Starting server with NewRelic..."
    echo "NewRelic Environment: $NEW_RELIC_ENVIRONMENT"
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn -b $S_ADDRESS:$PORT -w 3 --forwarded-allow-ips="*"  {{cookiecutter.module_name}}.wsgi
    exit_with_error
}

start_server(){
    echo "Starting gunicorn..."
    gunicorn -b $S_ADDRESS:$PORT -w 3 --forwarded-allow-ips="*"  {{cookiecutter.module_name}}.wsgi
}

start_server_in_development(){
    echo "Starting server in development mode..."
    DEBUG=True python manage.py runserver $S_ADDRESS:$PORT
    exit_with_error
}

start_server_as_rqw(){
    echo "Starting server as a rq-worker node..."
    python manage.py rqworker default
    exit_with_error
}

start_server_as_rqs(){
    echo "Starting server as a rq-scheduler node..."
    rqscheduler --host redis --verbose
    exit_with_error
}

wait_for_db(){
    echo "Waiting for PG to become online..."
    sleep 5
}

default_start(){    
    wait_for_db
    migrate_data
    start_server
    exit_with_error
}

migrate_data(){
    wipe_db && python manage.py makemigrations && python manage.py migrate && load_fixtures    
}

load_fixtures(){
    if [ $NO_FIXTURES -eq 0 ]; then echo "Loading fixtures from $FIXTURES_PATH" && python manage.py loaddata $FIXTURES_PATH && return; fi
    echo "Not loading any fixtures."    
}

wipe_db(){
    if [ $WIPE -eq 1 ]; then echo "Cleaning database before running migrations..." && python manage.py reset_db --close-sessions --noinput && return; fi    
}

schedule_tasks(){
    echo "Scheduling tasks..."
    python manage.py scheduler --all    
}

choose_starting_way(){

    if [ $RQW -eq 1 ]; then start_server_as_rqw; fi

    if [ $RQS -eq 1 ]; then start_server_as_rqs; fi

    if [ $RQT -eq 1 ]; then schedule_tasks; fi

    if [ $DEVELOPMENT -eq 1 ]; then wait_for_db && migrate_data && start_server_in_development || exit_with_error; fi

    if [ $NEW_RELIC -eq 1 ]; then wait_for_db && migrate_data && start_server_with_newrelic || exit_with_error; fi

    default_start
}

main(){
    choose_starting_way
}

# Loop through arguments and process them
for arg in "$@"
do
    case $arg in
        -h|--help)
        display_help
        shift
        ;;
        -n|--newrelic)
        NEW_RELIC=1
        shift # Remove --newrelic from processing
        ;;
        -w|--worker)
        RQW=1
        shift
        ;;
        -s|--scheduler)
        RQS=1
        shift
        ;;
        -t|--tasks)
        RQT=1
        shift
        ;;        
        -nf|--no-fixtures)
        NO_FIXTURES=1
        shift
        ;;
        -d|--development)
        DEVELOPMENT=1
        shift
        ;;
        -pf|--production-fixtures)
        FIXTURES_PATH='fixtures/production/*.json'
        shift
        ;;
        -w|--wipe)
        WIPE=1
        shift
        ;;
        -e=*|--nrenv=*)
        NEW_RELIC_ENVIRONMENT="${arg#*=}"
        shift
        ;;
        -p=*|--port=*)
        PORT="${arg#*=}"
        shift 
        ;;
        -a=*|--address=*)
        S_ADDRESS="${arg#*=}"
        shift 
        ;;
        *)
        exec "@"
        shift
        ;;
    esac
done

main
