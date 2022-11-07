def fibonacciN(step):
	
	fibonacciArray = [1, 1]
	
	if step<3:
		if step == 2:
			return fibonacciArray
		elif step == 1:
			return "[" + str(fibonacciArray[0]) + "]"
		else:
			return "Step count is illegal."
	else:
		var1, var2, checkpoint = 1,1,0
		for i in range(step-2):
			checkpoint = var1 + var2
			fibonacciArray.append(checkpoint)
			var1 = var2
			var2 = checkpoint
		return fibonacciArray

def fibonacciR(step):
	if step>=1:
		if step == 1: return 1
		if step == 2: return 1
		return fibonacciR(step-1) + fibonacciR(step-2)
	else:
		return "Step count is illegal"
