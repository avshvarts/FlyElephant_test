from time import time

time0 = time()

fout = open("FlyElephant_test.txt","w")
print >> fout, "Test string for FlyElephant"
print "Check the test file..."

fin = open("FlyElephant_test_input.txt","r")
for line in fin:
    print line

import numpy as np
print np.eye(3)

import pandas as pd
X = pd.DataFrame({"A":[1,2,3],"Score":[0,5,7]})
print "\n",X

from sklearn.linear_model import LogisticRegression
print "sklearn.linear_model.LogisticRegression imported"
print "finished in",time()-time0,"seconds"