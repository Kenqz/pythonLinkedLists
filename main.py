
# LinkedList interview prep

class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get(self,index):
		if index>=self.length() or index<0: 
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	def erase(self,index):
		if index>=self.length() or index<0: 
			print("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	def __getitem__(self,index):
		return self.get(index)


	
	def insert(self,index,data):
		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

	def insert_node(self,index,node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): 
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1


	def set(self,index,data):
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				cur_node.data=data
				return
			cur_idx+=1

mylist1 = linked_list()
mylist1.append(1)
mylist1.append(2)
mylist1.get(1)
mylist1.display()

