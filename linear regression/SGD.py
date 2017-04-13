import numpy
def SGD():
	x = [[1, 0., 2], [1, 1., 5], [1, 2., 4], [1, 3., 3], [1, 4., 2]]
	y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]
	alpha = 0.01
	epsilon = 0.00001
	m = len(x)
	theta = [0, 0, 0]
	error = 0
	count = 0
	thetaa = numpy.mat(theta).T
	xa = numpy.mat(x).T
	ya = numpy.mat(y).T
	while True:
		count += 1
		for i in range(m):
			bias = ya[i] - numpy.dot(thetaa.T,xa[:,i])
			thetaa = thetaa + alpha * xa[:,i] * bias
		error1 = 0
		for i in range(m):
			error1 += (ya[i] - numpy.dot(thetaa.T,xa[:,i])) ** 2 / 2
		if abs(error-error1) < epsilon :
			break
		else :
			error = error1
	print error1
	print thetaa
SGD()
