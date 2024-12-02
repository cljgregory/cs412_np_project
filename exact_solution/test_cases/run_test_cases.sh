#!/bin/bash

# Path to your Python program (adjust if necessary)
PROGRAM="../cs412_mingraphcolor_exact.py"

# Directory containing your test cases
TEST_CASES_DIR="./inputs"

# Output directory for results
OUTPUT_DIR="./outputs"
mkdir -p $OUTPUT_DIR

# Loop through all test case files in the input folder
for TEST_FILE in $TEST_CASES_DIR/*; do
    # Get the base name of the test case file
    BASE_NAME=$(basename $TEST_FILE)
    
    # Run the Python program, pass the test file as input, and redirect output to a result file
    echo "Running test case: $BASE_NAME"
    python3 $PROGRAM < $TEST_FILE > $OUTPUT_DIR/$BASE_NAME.out
    
    # Optional: Print output for verification
    echo "Output for $BASE_NAME:"
    cat $OUTPUT_DIR/$BASE_NAME.out
    echo "-----------------------------"
done

