#!/bin/bash

# to build, use this command: chmod +x run_test_cases.sh

# Path to your Python program (adjust if necessary)
PROGRAM="../cs412_mingraphcolor_approx.py"

# Directory containing your test cases
TEST_CASES_DIR="./inputs"
TEST_CASES_DIR_2="./BIG_inputs"

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

# For the really big files, output is not printed but the time and number of
# colors is displayed
for TEST_FILE in $TEST_CASES_DIR_2/*; do
    # Get the base name of the test case file
    BASE_NAME=$(basename $TEST_FILE)
    
    echo "Running test case: $BASE_NAME"
    start=$(date +%s.%N)
    output=$(python3 "$PROGRAM" < "$TEST_FILE") 
    end=$(date +%s.%N)
    runtime=$(echo "$end - $start" | bc)

    echo "$output" > "$OUTPUT_DIR/$BASE_NAME.out"

    printf "      Wall clock time for approx: %.6f seconds\n" "$runtime"
    echo "      Number of colors from approx: $(echo "$output" | head -n 1)"
    echo "-----------------------------"
done