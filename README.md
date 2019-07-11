# AML-2019-Group16




The 3D surface presentation of this function is as below:

<img src="https://github.com/jznyxmd/AML-2019-Group16/blob/master/Rosenbrock_Surface.png" width="400" height="300">

We experiment 11 different step size and the following plot shows its relationship with iteration number (limited up to 10,000).

<img src="https://github.com/jznyxmd/AML-2019-Group16/blob/master/nsteps_vs_stepsz.png" width="700" height="200">

It is noticeable that it’s difficult to converge with either too small or too big step size. 
Using step size 0.002075 (4304 steps), the path is as below:

![](https://github.com/jznyxmd/AML-2019-Group16/blob/master/gd_path.png)

The final error is  9.99e-05, which is acceptable. The path is stable; however, it becomes slow when entering the turning point and getting close to the target (1, 1) point.
The path of the other two GD variants are shown as below: 

![](https://github.com/jznyxmd/AML-2019-Group16/blob/master/agd_path.png)
![](https://github.com/jznyxmd/AML-2019-Group16/blob/master/ngd_path.png)


 
