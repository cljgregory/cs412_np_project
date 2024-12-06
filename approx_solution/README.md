Exact Solution commands and input
Command: python ./cs412_np_project/approx_solution/cs412_mingraphcolor_approx.py

First Line: Number of edges
The remaining lines describe an edge between 2 vertices in the graph

Example Input:
2
a b
b c

First line (2): Number of edges in the graph
Second line (a b): An edge between a and b
Third Line (b c): An edge between b and c

Example Output:
2
a 0
b 1
c 0

First line (2): Minimum number of colors in the graph
Second line (a 0): Vertex a colored "0"
Third line (b 1): Vertex b colored "1"
Fourth line (c 0): Vertex c colored "0"

All test files are located in "approx_solution/test_cases". Instructions:
    For all test cases:
        - run the "run_test_cases.sh" file.
        - Command: ./run_test_cases.sh
        - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, 
                     use this command: chmod +x run_test_cases.sh
    For the non_optimal case:
        - run the "run_nonopt_cases.sh" file.
        - Command: ./run_nonopt_cases.sh
        - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, 
                     use this command: chmod +x run_nonopt_cases.sh
    For seeing data used for the plots in the presenation:
        - run the "compute_approx_wallclock.sh" file.
        - Command: ./compute_approx_wallclock.sh
        - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, 
                     use this command: chmod +x compute_approx_wallclock.sh

All test files are located in "exact_solution/test_cases/inputs" and can be run using the "run_test_cases.sh" script
Command: ./run_test_cases.sh while in the test_cases folder

Note: test case 12_clique.txt takes more than 20 minutes to run! This applies for the run_test_cases.sh AND 
      the compute_approx_wallclock.sh files
