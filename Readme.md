# Numerical Algorithms 
## Cart Pole Swing Up Analysis
`Mayaank Ashok 2022111022`

`Abhinav Raundhal 2022101089`

## OptimTraj

The OptimTraj folder contains all the MATLAB codes to run the algorithm for finding
minimum force and minimum time for the Cart-Pole problem

Run the `MAIN_minForce.m` and `MAIN_minTime.m`

## Presentations

This folder contains 3 presentations of the project: initial, mid-evals and final

## Code

### Plots

This contains 3 plots for each minForce and minTime namely:
1. state
2. error
3. image

### Simulations

The simulations folder contains 3 folders: minforce, mintime and grid_mesh.  
First two contain the same file sim.py which can be run using python : python3 `sim.py`  
It takes in data from 3 matlab files t.mat, p1.mat and p2.mat  
t represents time  
p1 represents the position of the center of the cart  
p2 represents the position of the tip of the pendulum  
The output is the animation of the trajectory of the cart-pole  

The grid_mesh folder conatins analysis of time taken and error w.r.t. the number of grid points  
The trade off between time and error can be analysed through a graph plotted using 
`analysis.py`  
The plots for error are saved for points 10-60 with an interval of 5  


### Videos 

This folder contains the animations for minForce and minTime  

### References

The project is derived from - OptimTraj - https://github.com/MatthewPeterKelly/OptimTraj
