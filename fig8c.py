'''
Perform the transformation in Fig 8C of Ince et. al., (2017)
'''

import numpy       as     np 
import seaborn     as     sns
from   scipy.stats import rankdata, norm 

# Generating data
N = 1000 # Number of points
x = np.random.exponential(1.5, size=N)
y = x + np.random.normal(0,1,size=N)
# Getting data ranks
xr = rankdata(x).astype(int)
yr = rankdata(y).astype(int)
# Normalized ranks
xrn = xr / (N+1)
yrn = yr / (N+1)
# Inverse gaussian transform CDF
xri = norm.ppf(xrn)
yri = norm.ppf(yrn)



sns.jointplot(x, y, alpha=.6)


plt.scatter(xrn, yrn, alpha=.6)

sns.jointplot(xri, yri, alpha=.6)