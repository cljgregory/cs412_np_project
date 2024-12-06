Exact Solution commands and input <br />
Command: python ./cs412_np_project/approx_solution/cs412_mingraphcolor_approx.py<br />

First Line: Number of edges <br />
The remaining lines describe an edge between 2 vertices in the graph <br />

Example Input:<br />
2<br />
a b<br />
b c<br />

First line (2): Number of edges in the graph<br />
Second line (a b): An edge between a and b<br />
Third Line (b c): An edge between b and c<br />

Example Output:<br />
2<br />
a 0<br />
b 1<br />
c 0<br />

First line (2): Minimum number of colors in the graph<br />
Second line (a 0): Vertex a colored "0"<br />
Third line (b 1): Vertex b colored "1"<br />
Fourth line (c 0): Vertex c colored "0"<br />

All test files are located in "approx_solution/test_cases". Instructions:<br />
  - For all test cases:<br />
    - Run the "run_test_cases.sh" file.<br />
    - Command: ./run_test_cases.sh<br />
    - Note: for the large test cases, the .sh file will show that it runs fast and produces a number of colors
            but not show the vertex coloring (because it takes up a ton of space)<br />
    - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, <br />
                 use this command: chmod +x run_test_cases.sh<br />
  - For the non_optimal case:<br />
    - Run the "run_nonopt_cases.sh" file.<br />
    - Command: ./run_nonopt_cases.sh<br />
    - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, <br />
                 use this command: chmod +x run_nonopt_cases.sh<br />
  - For seeing data used for the plots in the presenation:<br />
    - Run the "compute_approx_wallclock.sh" file.<br />
    - Command: ./compute_approx_wallclock.sh<br />
    - Reminders: make sure that you are in the test_cases folder. You may need to build the file, if so, <br />
                 use this command: chmod +x compute_approx_wallclock.sh<br />

All test files are located in "exact_solution/test_cases/inputs" and can be run using the "run_test_cases.sh" script<br />
Command: ./run_test_cases.sh while in the test_cases folder<br />

Note: test case 12_clique.txt takes more than 20 minutes to run! This applies for the run_test_cases.sh AND <br />
      the compute_approx_wallclock.sh files.<br />
