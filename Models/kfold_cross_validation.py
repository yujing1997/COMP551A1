# -*- coding: utf-8 -*-
"""
K-fold cross validation:
    5-fold cross validation to estimate performance in all experiments
    evaluate the performance using accuracy 
    
    tasks: 
        1. Compare the accuracy of naive Bayes and logistic regression on the four datasets
        2. Test different learning rates for gradient descent appleid to logistic regression
        Use the threshold for change in the value of the cost function as termination criteria, 
        and plot the accuracy on train/validation set as a function of iterations of gradient descent. 
        3.  Compare the accuracy of the two models as a function of the size of dataset (by controlling the training size). 
        As an example, see Figure 1 here 1. 
"""


### k-fold cross validation 
# https://github.com/codebasics/py/blob/master/ML/12_KFold_Cross_Validation/12_k_fold.ipynb
# https://machinelearningmastery.com/implement-resampling-methods-scratch-python/

# We calculate the size of each fold as the size of the dataset divided by the number of folds required.

fold size = total rows / total folds
# If the dataset does not cleanly divide by the number of folds, 
# there may be some remainder rows and they will not be used in the split.
# We then create a list of rows with the required size and add them to a list of folds which is 
# then returned at the end.
from random import randrange

# Split a dataset into k folds
def kfold_cross_validation(dataset, folds=3):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / folds)
	for i in range(folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

from random import seed
from random import randrange

# try new 
# Split a dataset into k folds
def kfold_cross_validation(dataset, folds=3):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / folds)
	for i in range(folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# test cross validation split
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
folds = cross_validation_split(dataset, 4)
print(folds)    




