#fractional Knapsack
class ItemValue: 
	
	
	def __init__(self, wt, val, ind): 
		self.wt = wt 
		self.val = val 
		self.ind = ind 
		self.cost = val // wt 

    
	def __gt__(self, other): 
		return self.cost > other.cost 


class FractionalKnapSack: 
	
	@staticmethod
	def getMaxValue(wt, val, capacity): 
		
					
		iVal = [] 
		for i in range(len(wt)): 
			iVal.append(ItemValue(wt[i], val[i], i)) 

		# sorting items by value 
		iVal.sort(reverse = True) 
        # sort in decreasing order 
		totalValue = 0
        
		for i in iVal: 
			curWt = int(i.wt) 
			curVal = int(i.val) 
			if capacity - curWt >= 0: 
				capacity -= curWt 
				totalValue += curVal 
			else: 
				fraction = capacity / curWt 
				totalValue += curVal * fraction 
				capacity = int(capacity - (curWt * fraction)) 
				break
		return totalValue 

# Driver Code 
if __name__ == "__main__": 
	wt = [10, 40, 20, 30] 
	val = [60, 40, 100, 120] 
	capacity = 50

	maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity) 
	print("Maximum value in Knapsack =", maxValue) 


