# mode() function a sub-set of the statistics module 
'''
StatisticsError is raised while using mode when there are 
two equal modes present in a data set and when the data set 
is empty or null

Applications : The mode() is a statistics function and mostly used in Financial Sectors to compare values/prices with past details, calculate/predict probable future prices from a price distribution set. mean() is not used seperately but along with two other pillars of statistics mean and meadian creates a very powerful tool which can be used to reveal any aspect of your data.

'''
import statistics 

data =[1, 2, 5, 3, 4, 5, 4, 5, 5, 6]
# We can infer that 5 has the highest population distribution 

######mode  
# Printing out mode of given data-set 
print("Mode of given data set is % s" % (statistics.mode(data)))

####mean
x = statistics.mean(data) 
  
# Printing the mean 
print("Mean is :", x) 



##median
'''
Python statistics | median()
Python is a very popular language when it comes to data analysis and statistics. Luckily, Python3 provide statistics module, which comes with very useful functions like mean(), median(), mode() etc.

median() function in the statistics module can be used to calculate median value from an unsorted data-list. The biggest advantage of using median() function is that the data-list does not need to be sorted before being sent as parameter to the median() function.

Median is the value that separates the higher half of a data sample or probability distribution from the lower half. For a dataset, it may be thought as the middle value. The median is the measure of central tendency of the properties of a data-set in statistics and probability theory. Median has a very big advantage over Mean, which is the median value is not skewed so much by extremely large or small values. The median value is either contained in the data-set of values provided or it doesn’t sway too much from the data provided.

Applications :
For practical applications, different measures of dispersion and population tendency are compared on basis how well the corresponding population values can be estimated. For example, a comparison shows that sample mean is more statistically efficient than the sample median when the data is uncontaminated by data from heavily-tailed data distribution or from mixtures of data distribution, but less efficient otherwise and that the efficiency of the sample median is higher than that for a wide range of distributions. To be more specific, the median has 64% efficiency compared to minimum-variance-mean ( for large normal samples )

'''
print("Median of data-set is : % s "
        % (statistics.median(data))) 


##var
'''
Python statistics | variance()
Statistics module provides very powerful tools, which can be used to compute anything related to Statistics. variance() is one such function. This function helps to calculate the variance from a sample of data (sample is a subset of populated data).

variance() function should only be used when variance of a sample needs to be calculated. There’s another function known as pvariance(), which is used to calculate the variance of an entire population.

In pure statistics, variance is the squared deviation of a variable from its mean. Basically, it measures the spread of random data in a set from its mean or median value. A low value for variance indicates that the data are clustered together and are not spread apart widely, whereas a high value would indicate that the data in the given set are much more spread apart from the average value.
'''
# Creating a sample of data 
sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98] 
  
  
print("Variance of sample set is % s" 
      %(statistics.variance(sample)))


'''
Python statistics | stdev()
Statistics module in Python provides a function known as stdev() , which can be used to calculate the standard deviation. stdev() function only calculates standard deviation from a sample of data, rather than an entire population.
To calculate standard deviation of an entire population, another function known as pstdev() is used.

Standard Deviation is a measure of spread in Statistics. It is used to quantify the measure of spread, variation of a set of data values. It is very much similar to variance, gives the measure of deviation whereas variance provides the squared value.

Applications :

Standard Deviation is highly essential in the field of statistical maths and statistical study. It is commonly used to measure confidence in statistical calculations. For example, the margin of error in calculating marks of an exam is determined by calculating the expected standard deviation in the results if the same exam were to be conducted multiple times.
It is very useful in the field of financial studies as well as it helps to determine the margin of profit and loss. The standard deviation is also important, where the standard deviation on the rate of return on an investment is a measure of the volatility of the investment.


'''
print("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample)))




'''
def average(numbers, type=None):
import statistics
try:
    statistics.mean(numbers)
except:
    raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
if type == 'mean':
    return statistics.mean(numbers)
elif type == 'mode':
    return statistics.mode(numbers)
elif type == 'median':
    return statistics.median(numbers)
elif type == 'min':
    return min(numbers)
elif type == 'max':
    return max(numbers)
elif type == 'range':
    return max(numbers) - min(numbers)
elif type == None:
    return average(numbers, 'mean')
else:
    raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')
'''


import numpy as np
print (np.percentile([1,3,4,463,2,3,6,8,9,4,254,6,72], [0, 100]))













