#!/bin/bash

# to build, use this command: chmod +x compute_approx_wallclock.sh

# Path to your Python program (adjust if necessary)
APPROX_PROGRAM="../cs412_mingraphcolor_approx.py"
EXACT_PROGRAM="../cs412_mingraphcolor_exact.py"

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
    echo "Test case: $BASE_NAME"

    echo "  Running approx program..."
    start=$(date +%s.%N)
    output=$(python3 $APPROX_PROGRAM < $TEST_FILE) > $OUTPUT_DIR/approx_$BASE_NAME.out
    end=$(date +%s.%N)
    runtime=$(echo "$end - $start" | bc)
    
    echo "$output" > "$OUTPUT_DIR/approx_$BASE_NAME.out"

    echo "      Wall clock time for approx: %.6f seconds" $runtime
    echo "      Number of colors from approx: $(echo "$output" | head -n 1)"

    echo "  Running exact program..."
    start=$(date +%s.%N)
    output=$(python3 $EXACT_PROGRAM < $TEST_FILE) > $OUTPUT_DIR/exact_$BASE_NAME.out
    end=$(date +%s.%N)
    runtime=$(echo "$end - $start" | bc)

    echo "$output" > "$OUTPUT_DIR/exact_$BASE_NAME.out"

    echo "      Wall clock time for exact: %.6f seconds" $runtime
    echo "      Number of colors from exact: $(echo "$output" | head -n 1)"

    echo "------------------------------"
done
