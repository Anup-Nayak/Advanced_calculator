from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		self.li=[]
		pass

	def infixToPostfix(self,expression): 
		o = set(['+', '-', '*', '/', '(', ')', '^'])  
		p = {'+':1, '-':1, '*':2, '/':2, '^':3} 

		stack = Stack() 
		m=expression
		output = []
		
		n=[]
		
		for i in m:
			if i=="{":
				n.append("(")
			elif i=="}":
				n.append(")")
			else:
				n.append(i)
		
		for c in n:

			if c not in o:  

				output.append(c)

			elif c=='(':  
				stack.push('(')

			elif c==')':

				while stack and stack.peek()!= '(':

					output.append(stack.pop())

				stack.pop()

			else: 

				while stack and stack.peek()!='(' and p[c]<=p[stack.peek()]:

					output.append(stack.pop())

				stack.push(c)

		while stack:

			output.append(stack.pop())

		return output

	def centralfunc(self,ab):
			stack=Stack()
			for i in ab:
	
				
				try:
					stack.push(float(i))
				
				
				except ValueError:
					val1 = stack.pop()
					val2 = stack.pop()
					if i == '/':
						stack.push(val2 / val1)
					else:
						
						
						switcher = {'+': val2 + val1, '-': val2 -
									val1, '*': val2 * val1, '^': val2**val1}
						stack.push(switcher.get(i))
			return float(stack.pop())


	def evaluate_expression(self, input_expression):

		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		try:
			a=self.tokenize(input_expression)
			b=self.evaluate_list_tokens(a)
			self.li.append((input_expression,b))
			return b
		except:
			return "Error"
		pass
	
	
		
	def tokenize(self, input_expression):
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		s=input_expression
		s=s.replace(" ","")
		l=["+","-","/","*","(",")","{","}"]
		a=""
		
		for i in s:
			if i in l:
				a=a+" "+i+" "
			else:
				a+=i
		
		b=list(a.split())

		m=[]
		for i in b:	
			if i in l:
				m.append(i)
			else:
				m.append(int(i))
		return m

		pass		
	
	def check_brackets(self, list_tokens):
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		l=list_tokens
		stack=Stack()
		li=["(",")","{","}"]
		a=[]
		for i in l:
			if i in li:
				a.append(i)
		
		flag=True
		
		for i in a:
			if i=="{" and flag==False:
				return False
			elif i=="{":
				stack.push(i)
			elif i=="(":
				stack.push(i)
				flag=False
			elif i==")" and flag==False:
				stack.pop()
				if stack.peek()!="(":

					flag=True
			elif i==")":
				if stack.peek()!="(":
					return False
			
			elif i=="}":
				if stack.peek()!="{":
					return False
				else:
					while stack.peek()!="{":
						stack.pop()
					stack.pop()
		
		if stack.is_empty():
			return True
		else:
			return False
		
		
		
		
				

	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		calculator = AdvancedCalculator()
		answer = calculator.evaluate_expression("2 + (3 /4)") # answer should be 2.75
		answer = calculator.evaluate_expression("2 +") # answer should be "Error"
		tokens = calculator.tokenize("2 + 3") # tokens should be [2, '+', 3]
		answer = calculator.evaluate_list_tokens([2, '+', 3]) # answer should be 5.0
		correct_brackets = calculator.check_brackets(['(', 2, '*']) # should be False
		history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + (3 /4)", 2.75)]
		"""
		
		if not AdvancedCalculator.check_brackets(self,list_tokens):
			return "Error"
		else:
			try:
				a=self.infixToPostfix(list_tokens)
				b=self.centralfunc(a)
				return b
				pass

			except:
				return "Error"
				pass
			pass
			

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.li[::-1]
		pass

'''
calculator=AdvancedCalculator()
answer=calculator.evaluate_expression("(3+4)*{4/(3-7)}+((10-2)-2)")
print(calculator.tokenize("(3+4)*{4/(3-7)}+((10-2)-2)+88"))
print(answer)
#print(calculator.check_brackets(answer))
answer=calculator.evaluate_list_tokens([12, '+', 2, '-', '{', 7, '+', '(', 8, '*', 9, ')', '/', 6, '}'])
print(answer)
#print(calculator.tokenize("12+2-{7+(8*9)/6}"))'''