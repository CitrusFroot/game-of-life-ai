# game-of-life-ai
This project is a passion project to help improve my programming skills, my familiarity with Python,
and various forms of machine learning methods. It is my personal take on John Horton Conway's Game of Life.

The game consists of a simulation of 'cells', where each cell in the nxn grid follows the following rules:
-   Any live cell with fewer than two live neighbours dies
-   Any live cell with two or three live neighbours lives
-   Any live cell with more than three live neighbours dies
-   Any dead cell with exactly three live neighbours becomes a live cell
*note that dead refers to simply an empty cell

In this project, I will make 3 iterations of this game. The first will be the rules above. The second
will include the following rules:
-   Any live cell adjacent to a dead cell MAY move to that cell
-   Any live cell may die after a step due to it's lifespan
-   Any live cell adjacent to more than three neighbors MAY survive
-   Any live cell surrounded by eight live cells becomes a super-cell
-   Any live super-cell will decompose if one of it's nine cells dies
-   Any live super-cell MAY move to a free adjacent 3x3 area
-   Any live cell adjacent to a super-cell dies

In the third iteration, I will implement multiple machine learning models to optimize the options that these cells
have in my 2nd iteration. In the end, I will create a simulation and pit these different models against each other.
The models I will use are:
-   Perceptron (TLU)
-   Feed-Forward Neural Network (FFNN)
-   Deep Neural Network (DNN)
-   Convolutional Neural Network (CNN)
-   Recurrent Neural Network (RNN)
-   Random Forest (RF)
-   Linear Regression
-   APriori Algorithm
-   Principle Component Analysis (PCA)
-   NeuroEvolution of Augmenting Topologies (NEAT)
-   DeepQ learning
-   Deep Reinforcement learning (DRL)
*This list may change as development goes on. Some of these methods may simply be impossible given the input data,
 or there may be better options that I would like to try to implement

A version history doc will also be included in the project, as well as the saved models, my notes, research, and credits.

Please feel free to comment on the repo how I may optimize my code, other machine learning methods I should try,
or fork the project and try to do better!