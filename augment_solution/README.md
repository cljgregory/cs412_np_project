# cs412_np_project
Augmented Solution commands and input <br />
## Augmented Approximation Solution for Minimum Graph Coloring<br />

### Overview<br />
The **Augmented Approximation Solution** aims to enhance the basic approximation algorithms for the **Minimum Graph Coloring Problem** by incorporating additional heuristics and bounds. This augmentation leverages the **DSATUR (Degree of Saturation)** algorithm and computes **lower** and **upper bounds** to provide a more efficient and effective coloring strategy.

### Features<br />
- **DSATUR Coloring Algorithm**: An advanced heuristic that selects the next vertex to color based on the highest degree of saturation.
- **Bound Computation**: Calculates lower and upper bounds for the chromatic number to assess the quality of the coloring.
- **Runtime Measurement**: Tracks the execution time of the coloring process for performance analysis.
- **Test Case Automation**: Includes scripts to run multiple test cases and compare results across exact, approximate, and augmented solutions.

#### Running the Augmented Approximation Solution<br />
To execute the augmented approximation solution, use the following command:<br />
All test files are located in "augmented_solution/test_cases/inputs" and can be run using the "run_compare_test_cases.sh" script <br />
Command: ./run_test_cases.sh while in the test_cases folder

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
Fifth line (Elapsed Time...): Total time taken to run algorithm <br />








