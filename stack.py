class stack:
	def __init__(self):
		self.list=[];

	def push(self,data):
		self.list.append(data);
	
	def dis(self):
		i=0;
		while(i != len(self.list)):
			print(self.list[i],end=",");
			i=i+1;
	def pop(self):
		if len(self.list)<=0:
			print("Underflow occured");

		else:
			self.list.pop();

a=stack();
while(1):
	print();
	print("Enter 1 for PUSH:");
	print("Enter 2 for POP:");
	ch=input("Enter your chioce:");
	ch=int(ch);
	if ch == 1 :
		data=input("Enter a value to push:");
		a.push(data);
		a.dis();
	elif ch == 2 :
		a.pop();
		a.dis();
	else:
		print("Invalid choice");















class stack:
    def __init__(self):
		self.stk=[];

	def push(self,value):
		self.stk.append(value);
	
    def dis(self):
		i=0;
		while(i != len(self.stk)):
			print(self.stk[i],end=",");
			i=i+1;
	
    def pop(self):
		if len(self.stk)<=0:
			print("Underflow occured");
        else:
			self.stk.pop();

a=stack();
while(1):
	print();
	print("Enter 1 for PUSH:");
	print("Enter 2 for POP:");
	chioce=input("Enter your chioce:");
	chioce=int(chioce);
	if chioce == 1 :
		data=input("Enter a value to push:");
		a.push(data);
		a.dis();
	elif chioce == 2 :
		a.pop();
		a.dis();
	else:
		print("Invalid choice");
