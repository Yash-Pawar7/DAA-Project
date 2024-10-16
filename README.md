# Travelling Salesperson Problem (TSP) Solver

This project implements various algorithms to solve the **Travelling Salesperson Problem (TSP)**, focusing on both exact and approximation methods. It is a mini project developed as part of the Design and Analysis of Algorithms course.

## Algorithms Implemented

1. **Brute Force**:  
   An exact solution by evaluating all possible routes to find the shortest path. Suitable for small datasets due to its high time complexity.

2. **Held-Karp Dynamic Programming**:  
   An efficient exact algorithm using dynamic programming and bitmasking. Significantly reduces redundant calculations by breaking down the problem.

3. **Nearest Neighbor Heuristic**:  
   A simple approximation algorithm that starts from a city and visits the nearest unvisited city until the tour is complete. Provides a quick solution, though not necessarily optimal.

4. **Genetic Algorithm**:  
   A population-based approximation algorithm that uses concepts from natural selection to evolve better solutions over generations. Balances between efficiency and accuracy for larger datasets.

## How to Run

To run the program, ensure you have Python installed and the required library `deap` for the genetic algorithm:

```bash
pip install deap

