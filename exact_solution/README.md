# cs412_np_project
Exact Solution commands and input <br />
Command: python ./cs412_np_project/exact_solution/cs412_mingraphcolor_exact.py <br />

First Line: Number of edges <br />
The remaining lines describe an edge between 2 vertices in the graph <br />

Example Input:
2 <br />
a b <br />
b c <br />

First line (2): Number of edges in the graph <br />
Second line (a b): An edge between a and b <br />
Third Line (b c): An edge between b and c <br />
 
Example Output:
2 <br />
a 0 <br />
b 1 <br />
c 0 <br />
Elapsed Time: XXX minutes XXX seconds <br />

First line (2): Minimum number of colors in the graph <br />
Second line (a 0): Vertex a colored "0" <br />
Third line (b 1): Vertex b colored "1" <br />
Fourth line (c 0): Vertex c colored "0" <br />
Fifith line (Elapsed Time...): Total time taken to run algorithm <br />

All test files are located in "exact_solution/test_cases/inputs" and can be run using the "run_test_cases.sh" script <br />
Command: ./run_test_cases.sh while in the test_cases folder






