# Calculating the variance in the spins for a microstate

We are now going to take the calculation of spin a little further.  Instead of calculating the average spin, we would like to calculate the variance for the spins.   The variance for these spins will be calculated as:

![](https://render.githubusercontent.com/render/math?math=\langle(s-\langle\s\rangle)^2\rangle=\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)^2

Once again the sum here runs over the ![](https://render.githubusercontent.com/render/math?math=N) spins in the system and the ![](https://render.githubusercontent.com/render/math?math=s_i) values are the spin coordinates once more.  Notice, however, that you need to calculate the average spin ![](https://render.githubusercontent.com/render/math?math=\langle\s\rangle) __before__ you calculate the summation here.

To summarise then, in order to complete the exercise, you need to write a function called `variance_spin`.  The input to your program will the spin coordinates for a particular microstate.  Your program should then compute the variance for the input set of spin variables. 
