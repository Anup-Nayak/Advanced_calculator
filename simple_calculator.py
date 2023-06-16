from stack import Stack

class SimpleCalculator:
	def __init__(self):
		"""
		Instantiate any data attributes
		"""
		self.li=[]
		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		s=input_expression
		l=["+","-","/","*"]
		flag=0
		for i in s:
			if ord(i)>=48 and ord(i)<=57 and flag == 0:
				flag= 1
			if i in l:
				flag=0
			elif ord(i)>=48 and ord(i)<=57 and flag == 1:
				pass
			elif i==" " and flag == 1:
				flag= 2
			elif ord(i)>=48 and ord(i)<=57 and flag == 2:
				return "Error"
			else:
				pass
			

		

		s=s.replace(" ","")
		
		count=0
		indi=0
		
		for i in s :
			
			if i in l:
				indi=s.index(i)
				count+=1
			
		
		if count!=1 and indi!=0 :
			self.li.append((input_expression,"Error"))
			return "Error"
		else:
			try:
				
				a=int(s[:indi])
				b=int(s[indi+1:])
				
				
				
				if s[indi]=="+":
					c= float(a+b)
					self.li.append((input_expression,c))
					return c
				elif s[indi]=="-":
					c= float(a-b)
					self.li.append((input_expression,c))
					return c
				elif s[indi]=="*":
					c= float(a*b)
					self.li.append((input_expression,c))
					return c
				else:
					c= float(a/b)
					self.li.append((input_expression,c))
					return c
				
				
			except:
				self.li.append((input_expression,"Error"))
				return "Error"
			

		pass

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		a=self.li
		return a[::-1]
		pass

