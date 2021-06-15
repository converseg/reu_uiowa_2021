import numpy as np
import csv
import pandas as pd
# these will probably be helpful, use whatever other libraries you like

# Might be best to do this inside of a CoLab notebook so you can look at the data more dynamically

# Data available at https://www.kaggle.com/tunguz/big-five-personality-test

# Read in CSV file
# data = pd.read_csv(path/to/big5_data.csv)

# that data has a bunch of columns, we don't need all of them
# responses = ... grab responses columns only, put into np matrix
# for a questionnaire with n questions and N examinees, we should have a (n x N) matrix

# compute some sort of simple measure to compare our results against
# e.g. for each student, sum their responses grouped by the category (EXT, AGR, etc)

# not super important, but it may be interesting to plot a histogram of each item to observe the general layout of the data.
# e.g. maybe almost all people answer the item "I insult people" as a "1", while other questions are answered more uniformly 1-5

# each element in the matrix is an integer {1,2,3,4,5} -- we should rescale this to be either binary (0 or 1) or continuous in interval [0,1]

# split data into Training set and Test set (we can do validation set using Keras while training)
# We can also consider doing some 5-fold cross validation -- maybe later 

# save each set of data into its own CSV or np file for use later

