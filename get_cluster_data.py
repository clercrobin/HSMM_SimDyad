
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

matLevel = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2])

matValues = np.array([
[1.775,0.838,2.078,1.105,0.059,0.475,0.18,0.502,1.171,2.908,2.75,0.059,0.18,1.12,0.056,1.926,0.584,30.5,8,0.477],
[3.801,1.104,2.659,0.904,0.766,0.603,0.146,0.565,0.7,0.275,0.293,0.766,0.146,-1.66,-0.064,3.23,0.855,493,114,0.541],
[1.105,0.595,3.271,0.975,0.04,0.464,1.497,0.498,2.96,16.635,15.5,0.04,1.497,3.616,0.071,2.188,0.604,59,15,0.492],
[3.842,3.235,4.199,2.058,1.092,0.829,2.978,0.643,1.093,1.113,1.434,1.092,2.978,1.003,-0.254,4.021,2.322,1236,219,0.705],
[4.427,0.909,3,0,6.702,0.58,0.003,0,0.678,0,0.003,6.702,0.003,-7.791,0.0,3.713,0.455,1201.5,314,0.478],
[4.064,1.148,3.817,1.717,1.155,0.623,0.732,0.669,0.939,0.847,0.789,1.155,0.732,-0.456,0.071,3.94,1.086,1155.5,265,0.545],
[6.03,1.461,6.177,1.724,14.739,0.781,8.784,0.815,1.024,1,0.959,14.739,8.784,-0.518,0.043,6.104,1.468,2171,349,0.778],
[5.199,2.314,5.366,1.276,2.851,0.795,21.625,0.682,1.032,1.109,1.291,2.851,21.625,2.026,-0.152,5.283,1.484,1806.5,326,0.693],
[4.311,1.452,4.369,1.142,1.597,0.664,3.298,0.606,1.014,1.139,1.248,1.597,3.298,0.725,-0.091,4.34,0.933,1432.5,314,0.57],
[2.884,1.623,3.629,1.074,0.792,0.551,2.584,0.518,1.258,1.535,1.631,0.792,2.584,1.182,-0.061,3.256,0.906,682.5,167,0.511],
[2.05,0.992,3.064,1.794,0.052,0.549,0.661,0.617,1.495,9,8,0.052,0.661,2.536,0.118,2.557,0.956,446.5,122,0.457],
[4.022,0.619,3.486,0.853,7.395,0.521,1.82,0.498,0.867,0.7,0.733,7.395,1.82,-1.402,-0.046,3.754,0.546,1225,313,0.489],
[1.997,1.992,3.736,2.236,0.168,0.774,1.111,0.699,1.871,3.298,3.654,0.168,1.111,1.887,-0.102,2.867,1.857,684.5,146,0.586],
[2.03,1.217,1.751,1.323,0.27,0.511,0.175,0.491,0.862,0.673,0.701,0.27,0.175,-0.432,-0.041,1.891,0.708,16,4,0.5],
[4.681,0.764,5.147,1.034,31.818,0.59,29.083,0.651,1.1,1.1,0.997,31.818,29.083,-0.09,0.098,4.914,0.794,1751,354,0.618],
[4.919,1.305,5.558,1.084,5.017,0.661,361,0.693,1.13,1.258,1.199,5.017,361,4.276,0.048,5.239,0.92,1886,360,0.655],
[3.945,2.623,2.997,1.611,1.034,0.772,0.749,0.561,0.76,0.612,0.842,1.034,0.749,-0.322,-0.319,3.471,1.504,871.5,186,0.586],
[4.705,0.891,3.031,1.764,23,0.596,0.272,0.763,0.644,0.286,0.223,23,0.272,-4.437,0.248,3.868,1.199,1005.5,230,0.546],
[4.258,1.098,5.066,1.511,3.827,0.581,4.324,0.697,1.19,1.23,1.024,3.827,4.324,0.122,0.183,4.662,1.147,1575.5,320,0.615],
[5.34,2.833,6.127,1.071,2.202,0.879,333,0.764,1.147,1.263,1.454,2.202,333,5.019,-0.141,5.733,1.581,1825.5,303,0.753],
[4.094,0.555,6.836,1.175,10.645,0.523,35.1,0.868,1.67,1.764,1.064,10.645,35.1,1.193,0.506,5.465,0.639,1959.5,357,0.686],
[5.837,1.976,6.452,1.22,4.569,0.805,59.333,0.811,1.105,1.208,1.199,4.569,59.333,2.564,0.008,6.144,1.221,2218,361,0.768],
[4.058,0.581,5.449,1.267,7.227,0.525,31.909,0.689,1.343,1.449,1.104,7.227,31.909,1.485,0.272,4.753,0.769,1707,358,0.596],
[5.183,1.302,4.514,1.449,29.083,0.655,2.8,0.643,0.871,0.748,0.762,29.083,2.8,-2.341,-0.019,4.849,0.883,1722.5,352,0.612],
[5.092,2.173,5.1,2.021,2.684,0.771,3.513,0.743,1.002,1.03,1.068,2.684,3.513,0.269,-0.037,5.096,1.688,1696.5,302,0.702],
[6.142,0.856,5.35,1.821,361,0.766,4.085,0.748,0.871,0.785,0.803,361,4.085,-4.482,-0.023,5.746,1.092,2065.5,359,0.719],
[3.208,0.773,7.197,1.316,0.664,0.499,361,0.897,2.243,4.506,2.507,0.664,361,6.299,0.586,5.203,0.753,1873,360,0.65],
[4.819,1.496,3.508,1.847,5.119,0.657,0.687,0.707,0.728,0.524,0.487,5.119,0.687,-2.008,0.074,4.164,1.39,1254.5,264,0.594],
[3.839,0.922,3.263,1.182,2.261,0.541,0.574,0.562,0.85,0.546,0.526,2.261,0.574,-1.371,0.037,3.551,0.786,841,208,0.505],
[4.086,1.375,5.583,2.194,1.616,0.62,5.446,0.78,1.366,1.722,1.368,1.616,5.446,1.215,0.23,4.835,1.323,1586.5,307,0.646]])

def update_position(e):
   print "From update position"
   #Transform co-ordinates to get new 2D projection
   tX, tY, _ = proj3d.proj_transform(dataX, dataY, dataZ, ax.get_proj())
   for i in range(len(dataX)):
      label = labels[i]
      label.xy = tX[i],tY[i]
      label.update_positions(fig.canvas.renderer)
   fig.canvas.draw()
   return



X = matValues

valueExtract = []
#for j in range(len(matValues)):
   #valueExtract.append([matValues[j][4],
                  #matValues[j][5],
                  #matValues[j][6],
                  #matValues[j][7],
                  #matValues[j][13]])
for j in range(len(matValues)):
   valueExtract.append([matValues[j][4],
                        matValues[j][6],
                        matValues[j][7],
                        matValues[j][13]])
centers = [[1, 1], [-1, -1], [1, -1]]
X = np.array(valueExtract) #matValues
y = matLevel

estimators = {'k_means_3': KMeans(3),
              'k_means_4': KMeans(4),
              'k_means_bad_init': KMeans(3, n_init=1,
                                         init='random')}


fignum = 1
for name, est in estimators.iteritems():
   fig = pl.figure(fignum, figsize=(4, 3))
   pl.clf()
   ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

   pl.cla()
   est.fit(X)
   labels = est.labels_

   print X[:,3]

   ax.scatter(X[:, 3], X[:, 0], X[:, 2], s = 120, c=labels.astype(np.float))

   ax.w_xaxis.set_ticklabels([])
   ax.w_yaxis.set_ticklabels([])
   ax.w_zaxis.set_ticklabels([])
   ax.set_xlabel('m_nonpos_pos_ratio')
   ax.set_ylabel('f_nonpos_pos_ratio')
   ax.set_zlabel('f_nonpos_propOfMax')
   fignum = fignum + 1

# Plot the ground truth
fig = pl.figure(fignum, figsize=(4, 3))
pl.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

pl.cla()
labels = ['point{0}'.format(i) for i in range(30)]

#for name, label in [('High', 0),
               #('Medium', 1),
               #('Low', 2)]:
   #ax.text3D(X[y == label, 3].mean(),
            #X[y == label, 0].mean() + 1.5,
            #X[y == label, 2].mean(), name,
            #horizontalalignment='center',
            #bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))

## Reorder the labels to have colors matching the cluster results
#y = np.choose(y, [1, 2, 0]).astype(np.float)

ax.scatter(X[:, 3], X[:, 0], X[:, 2], s = 120,c=y)


ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('m_nonpos_pos_ratio')
ax.set_ylabel('f_nonpos_pos_ratio')
ax.set_zlabel('f_nonpos_propOfMax')

dataX = X[:,3]
dataY = X[:,0]
dataZ = X[:,2]

#Transform co-ordinates to get initial 2D projection
tX, tY, _ = proj3d.proj_transform(dataX, dataY, dataZ, ax.get_proj())


#Array of labels
labels = []

#Loop through data points to initially annotate scatter plot
#and populate labels array

labelit = []
for i in range(len(X)):
   labelit.append(str(i))
for i in range(len(dataX)):
   #text='['+str(int(dataX[i]))+','+str(int(dataY[i]))+','+str(int(dataZ[i]))+']'  
   text = labelit[i]
   label = ax.annotate(text,
                       xycoords='data',
                       xy = (tX[i], tY[i]), xytext = (-20, 20),
                       textcoords = 'offset points', ha = 'right', va = 'top', fontsize=6,
                       bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                       arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
   labels.append(label)

#Positions are updated when mouse button is released after rotation.
fig.canvas.mpl_connect('button_release_event', update_position)

pl.show()