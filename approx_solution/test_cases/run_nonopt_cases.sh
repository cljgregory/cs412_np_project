#!/bin/bash

# to build, use this command: chmod +x run_nonopt_cases.sh

# Path to your Python program (adjust if necessary)
PROGRAM="../cs412_mingraphcolor_approx.py"

# Directory containing your test cases
TEST_CASES_DIR="./nonopt_input"

# Output directory for results
OUTPUT_DIR="./nonopt_output"
mkdir -p $OUTPUT_DIR

# Loop through all test case files in the input folder
for TEST_FILE in $TEST_CASES_DIR/*; do
    # Get the base name of the test case file
    BASE_NAME=$(basename $TEST_FILE)
    
    # Run the Python program, pass the test file as input, and redirect output to a result file
    echo "Running test case: $BASE_NAME"
    python3 $PROGRAM < $TEST_FILE > $OUTPUT_DIR/$BASE_NAME.out
    
    # What we should expect
    echo " "
    echo "Output we are expecting:"
    echo "3"
    echo "a 0"
    echo "b 1"
    echo "c 2"
    echo "d 0"
    echo "e 1"
    echo " "

    # Optional: Print output for verification
    echo "Actual output for $BASE_NAME:"
    cat $OUTPUT_DIR/$BASE_NAME.out
done