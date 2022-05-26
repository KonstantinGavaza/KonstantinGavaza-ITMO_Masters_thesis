# ITMO Masters thesis
ITMO Master's thesis 
Topic: Optimization of wells and roads to maximize oil production

Problem: The currently publicly available solutions to the problem of the optimal location of oil wells rely mainly on the volume of oil production, but do not consider the location of wells relative to geographical objects and technical restrictions on their location and construction. For instance, such solutions do not consider hard-to-reach points for the construction, shape and location of technical roads.

The purpose of this work is to develop and analyze the effectiveness of a cooperative optimization algorithm for the location of wells and roads in an oil field, considering inaccessible areas in which roads and wells cannot be built. Inaccessible areas combine geographical features that make it difficult to build on the field. To analyze the effectiveness of the cooperative algorithm, several other approaches have been developed as a comparison: \
●	"A naive approach without taking into account roads."  Separate optimization of the location of wells without considering roads. And the construction of roads through all wells after their optimization. \
●	"Consistent optimization of wells and roads". This approach is based on two stages. During the first stage, there is a separate optimization of the location of wells without considering roads. At the second stage, a separate optimization of roads takes place, considering the already optimized location of wells

For each of the three approaches, two options will be considered as the basic optimization algorithm: 
●	optimization using a variation of the genetic algorithm;
●	optimization using a variation of the PSO algorithm.

Objectives of study:
1.	Conducting a literature review on the topics: \
●	optimization of the placement of wells in the field;\
●	optimization of linear objects;\
●	application of joint optimization algorithms.\
2.	Search for oil field data in open sources for further experiments.\
3.	Developing a naive approach: optimizing the location of wells and building roads through them without inaccessible points.\
4.	Development of an evolutionary algorithm for optimizing the location of wells in the field.\
5.	Development of an evolutionary algorithm to optimize the location of roads in the field.\
6.	Development of a cooperative algorithm for optimizing wells and roads in the field.\
7.	Analysis of the effectiveness of the cooperative algorithm:\
●	convergence analysis of the cooperative algorithm;\
●	comparison of the results with the sequential application of the algorithms from points 3 and 4.



