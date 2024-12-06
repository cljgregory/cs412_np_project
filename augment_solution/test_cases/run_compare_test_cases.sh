#!/bin/bash

# ENSURE the script is executable
# chmod +x run_compare_test_cases.sh

# path to exact solution, approx solution, and augmented solution
EXACT_PROGRAM="../../exact_solution/cs412_mingraphcolor_exact.py"
APPROX_PROGRAM="../../approx_solution/cs412_mingraphcolor_approx.py"
AUGMENT_PROGRAM="../cs412_mingraphcolor_augment.py"

# Directory containing test cases
TEST_CASES_DIR="./inputs"

# Output directory for comparison results
OUTPUT_DIR="./outputs"
mkdir -p $OUTPUT_DIR

# Header for the comparison results
     echo -e "Test Case\tExact Colors\tApprox Colors\tAugment Colors\tExact Time\tApprox Time\tAugment Time\tLower Bound\tUpper Bound" > $OUTPUT_DIR/comparison_results.tsv



# Loop through all test case files in the input folder
for TEST_FILE in $TEST_CASES_DIR/*; do
    # Get the base name of the test case file
    BASE_NAME=$(basename $TEST_FILE)
    
    echo "Running test case: $BASE_NAME"
    #cat $TEST_FILE

    # Run Exact Solution
    EXACT_OUTPUT=$(python3 $EXACT_PROGRAM < $TEST_FILE 2>&1)
    EXACT_COLORS=$(echo "$EXACT_OUTPUT" | head -n 1)
    EXACT_TIME=$(echo "$EXACT_OUTPUT" | grep "Elapsed time" | awk '{print $3 " " $4}')

    # Run Approximation Solution
    APPROX_OUTPUT=$(python3 $APPROX_PROGRAM < $TEST_FILE 2>&1)
    APPROX_COLORS=$(echo "$APPROX_OUTPUT" | head -n 1)
    APPROX_TIME=$(echo "$APPROX_OUTPUT" | grep "Elapsed time" | awk '{print $3 " " $4}')

    # Run Augmented Approximation Solution
    AUGMENT_OUTPUT=$(python3 $AUGMENT_PROGRAM < $TEST_FILE 2>&1)
    AUGMENT_COLORS=$(echo "$AUGMENT_OUTPUT" | head -n 1)
    AUGMENT_TIME=$(echo "$AUGMENT_OUTPUT" | grep "Elapsed time" | awk '{print $3 " " $4}')

    # Capture lower and upper bounds from augmented solution output
    LOWER_BOUND=$(echo "$AUGMENT_OUTPUT" | grep "Lower Bound" | awk '{print $3}')
    UPPER_BOUND=$(echo "$AUGMENT_OUTPUT" | grep "Upper Bound" | awk '{print $3}')

    # Append to the comparison results
    echo -e "${BASE_NAME}\t${EXACT_COLORS}\t${APPROX_COLORS}\t${AUGMENT_COLORS}\t${EXACT_TIME}\t${APPROX_TIME}\t${AUGMENT_TIME}\t${LOWER_BOUND}\t${UPPER_BOUND}" >> $OUTPUT_DIR/comparison_results.tsv

    # Print output for verification (debug)
    echo "Exact Colors: $EXACT_COLORS, Time: $EXACT_TIME"
    echo "Approx Colors: $APPROX_COLORS, Time: $APPROX_TIME"
    echo "Augment Colors: $AUGMENT_COLORS, Time: $AUGMENT_TIME"
    echo "Lower Bound: $LOWER_BOUND"
    echo "Upper Bound: $UPPER_BOUND"
    echo "-----------------------------"
done
