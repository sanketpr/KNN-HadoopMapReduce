# KNN-HadoopMapReduce
Classification of data using k-NN, Implemented using Hadoop MapReduce

### setup.py:
- This file contains the driver code
- It reads the test data and pass each data point features to mapper in sys arguments
- Then it initiates map-reduce operation
- And at the last it combines all the output into a single file

### mapper-knn.py:
- The mapper takes one data point in system argument
- And in STDIN we pass it the training file
- For each training point we calculate the distance of the test data point
- Finally we output the distance value as the key and value as the the test data row along with the label of the compared data point in the training data.

### reducer-knn.py:
- The output of the mapper is given as input to reducer.py, so it receives distance as key and the value is the test data row for which the prediction is to be made
- The reducer groups the input data by the data rows in test data
- So for our given test data we will have 15 groups and each group will have the corresponding distance with each data point
- For our purpose we have statically set the value of k in reducer
- The reducer receives the data already sorted by the values of the key, and for our purpose the key was the distance.
- Therefore each group will be sorted according to distances with the data points in training data. So all we have to do is pick first K rows in each group.
- Since we have already appended the neighbors class labels to the row, we pick the suitable label from those K closest class labels.

### combiner.py
 - This part combines all the results and writes the result to a csv file
