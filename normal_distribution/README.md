# Normal Distribution
## about
this package is for solving gaussian distribution and finds attributes of data like mean, standard diviation and probability density
## why?
i made this package as a practice of my software engineering skills and also to get practice of math required for machine learning and to get a full expericence of publishing a fully rounded project into people.

it was a great experence building this project.
## preinstallments
it requires matplotlib to be preinstall as this package is able to plot the probability distribution function and other plots with the help of matplotlib library.

## features
this package can read a text file containing the data and perform distribution functions and plot the distribution graph.

## installation
`pip install normal-distribution` or you can also clone [github repo](https://github.com/kishoreKunisetty/normal_distribution) and run `pip install .` in the terminal when the terminal is inside normal_distribution folder.
## how to use?
importing and creating a gaussian 
```python
import normal_distribution as nd
gaussian = nd.Gaussian(25, 5)
gaussian
>>> mean 25, standard deviation 5
```
reading a data file in text format
```python
file_name = "file_location/file_name.txt"
gaussian.read_data_file(file_name)
```
calculating mean and standard deviation for the data.
```python
gaussian.calculate_mean()
gaussian.calculate_stdev()
```
plotting a histogram of the data
```
gaussian.plot_histogram()
```
>output

![figure1](Desktop/Figure_1.png)


## reference 
refer [github](https://github.com/kishoreKunisetty/normal_distribution) for mathematics behind this library 

