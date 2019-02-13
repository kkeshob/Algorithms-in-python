class node:
	def __init__(self,data):
		self.data=data;
		self.next=None;

def insert_last(head,data):
	if(head==None):
		head=node(data);
		return head;
	else:
		new=node(data);
		temp=head;
		while (temp.next != None):
			temp=temp.next;
		
		temp.next=new;
		return head;
def insert_first(head,data):
	if(head==None):
		head=node(data);
		return head;
	else:
		new=node(data);
		new.next=head;
		head=new;
		return head;
def insert_ap(head,data,pos):
	if(pos==1):		
		if(head==None):
			head=node(data);
			return head;
		else:
			new=node(data);
			new.next=head;
			head=new;
			return head;
	else:
		new=node(data);
		temp=head;
		i=1
		while (i<=pos-2):
			temp=temp.next;
			i=i+1;
		temp2=temp.next;
		temp.next=new;
		new.next=temp2;
		return head;	
def delete_last(head):
	if(head==None):
		print("There is no node..");
	else:
		temp=head;
		while (temp.next.next != None):
			temp=temp.next;
		
		temp.next=None;
		return head;
def delete_first(head):
	if(head==None):
		print("There is no node..");
	else:
		head=head.next;
		return head;
def delete_ap(head,pos):
	if(pos==1):		
		if(head==None):
			print("There is no node..");
		else:
			head=head.next;
			return head;
	else:
		temp=head;
		i=1
		while (i<=pos-2):
			temp=temp.next;
			i=i+1;
		temp.next=temp.next.next;
		return head;	
def dis(head):
	temp=head;
	while(temp != None):
		print(temp.data,end=" ");
		temp=temp.next;


head=None;
while(1):
	print();
	print("Enter 1 for Insert First:");
	print("Enter 2 for Delete First:");
	print("Enter 3 for Insert Last:");
	print("Enter 4 for Delete Last:");
	print("Enter 5 for Insert Any Position:");
	print("Enter 6 for Delete Any Position:");
	ch=input("Enter your chioce:");
	ch=int(ch);
	if ch == 1 :
		data=input("Enter a value to Insert:");
		head=insert_first(head,data);
		dis(head);
	elif ch == 2 :
		head=delete_first(head);
		dis(head);
	elif ch == 3 :
		data=input("Enter a value to Insert:");
		head=insert_last(head,data);
		dis(head);
	elif ch == 4 :
		head=delete_last(head);
		dis(head);
	elif ch == 5 :
		data=input("Enter a value to Insert:");
		pos=input("Enter a Position:");
		pos=int(pos);
		head=insert_ap(head,data,pos);
		dis(head);
	elif ch == 6 :
		pos=input("Enter a Position:");
		pos=int(pos);
		head=delete_ap(head,pos);
		dis(head);
	else:
		print("Invalid choice");