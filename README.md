# AML-2019-Group16
Many machine learning problems involve making a good prediction by learning from history data. A loss function tells us “how good” the prediction made by our model for a given set of parameters. The smaller the loss function, the smaller the error in prediction. As an algorithm, Gradient descent finds the optimisation to minimise some function by each step iteratively. Thus, Gradient descent is important in machine learning to help with finding the parameters that minimize the loss function.

Suppose a person is trapped in the mountains and needs to walk down towards the lowest point of the mountain. Based on his current location, the vanilla gradient descent algorithm looks for the steepest direction (optimal direction to get downhill) and take a step downward. The man will finally reach a position where he can no longer move downhill using the same method repeatedly for every step.
AdaGrad Algorithm and Nesterov Accelerated Gradient (NAG) Method are two modiﬁcations for plain vanilla gradient descent.

The AdaGrad algorithm optimizes the vanilla gradient descent method by changing the size of each step. Instead of using fixed size, AdaGrad Algorithm will cache all past steepness as a reference to see if the current steepness is relatively greater or less and adjust the step size adaptively. When the moving direction of current position is very steep, it will use a lager step. Otherwise, it will move less distance.

The Momentum method takes the speed of moving into account by using a momentum factor, which helps with accelerating the ‘walk-down process’. The NAG method is an improved version of the Momentum method, which considers the steepest direction of “the projected position” (one step forward) instead of exact current position. This can prevent the process from going too fast or missing the lowest point and thus get better control.

To illustrate GD process, we choose Rosenbrock function in two-dimensional form:

***f(x,y)=(1-x)^2+100(y-x^2)^2***

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

The animation of the path can be found in codes and summarized as follows:
