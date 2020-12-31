#!/bin/bash

run_tests(){
    pytest --cov=. --cov-report=term --cov-fail-under=100 --nomigrations
}

main(){    
    echo "Waiting db..."
    sleep 5
    echo "Running tests..."    
    run_tests 
}

main
