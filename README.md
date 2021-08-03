# Implementation of Single Source Shortest Path on FPGA using Bellman-Ford algorithm
Designed, simulated and implemented in hardware the graph traversal using BellmanFord Algorithm after exploiting the parallelism of the algorithm.

Link to video URL - 
https://drive.google.com/file/d/1YuxDx5EZi-UBSnSDmyP1GB7rpo_oOVJW/view?usp=sharing

![alt text](https://github.com/arjun1995237/EE705_course-project/blob/main/result_after_computation.jpeg?raw=true)

#Source index and Destination index is specified, then after computation, we get to see the shortest path on VGA monitor.
 -Note the functionalities of the following scripts;
  1-graph_gen.py----> will create the generate the info of the graph {weight btw egdes(4 bits),source index(5 bits),destination index(5 bits)} to be stored in the ROM present in computation section. Size of the ROM is 32x14 bits.
  2-



