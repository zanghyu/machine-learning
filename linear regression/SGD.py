import numpy
def SGD():
	# x有3个属性，共有5个x样本
	x = [[1, 0., 2], [1, 1., 5], [1, 2., 4], [1, 3., 3], [1, 4., 2]]
		
	y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]
	# alpha为学习率	
	alpha = 0.01
	# 当计算的误差之间差值小于epsilon时，停止学习
	epsilon = 0.00001
	# m为样本个数
	m = len(x)
	theta = [0, 0, 0]
	error = 0
	count = 0
	#首先将所有向量表示为列向量形式
	thetaa = numpy.mat(theta).T
	xa = numpy.mat(x).T
	ya = numpy.mat(y).T
	while True:
		count += 1
		for i in range(m):
			#这里使用numpy中的点乘，通过xa[:,i]选取第i列向量
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
