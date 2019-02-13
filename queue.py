class queue:
	def __init__(self):
		self.list=[];
	def enqueue(self,data):
		self.list.insert(0,data);
	def dequeue(self):
		if(len(self.list) <=0):
			print("Queue is Empty!");
		else:
			self.list.pop();
	def dis(self):
		i=0;
		while(i != len(self.list)):
			print(self.list[i],end=",");
			i=i+1;
a=queue();
while(1):
	print();
	print("Enter 1 for ENQUEUE:");
	print("Enter 2 for DEQUEUE:");
	ch=input("Enter your chioce:");
	ch=int(ch);
	if ch == 1 :
		data=input("Enter a value to ENQUEUE:");
		a.enqueue(data);
		a.dis();
	elif ch == 2 :
		a.dequeue();
		a.dis();
	else:
		print("Invalid choice");