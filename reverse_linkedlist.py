#reversing the linked list
class Node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__ (self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            val=int(input("enter data:"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new_node
            i=i+1
    def show (self,head):
        t=head
        while t:
            print(t.val,end=" ,")
            t=t.next
    def reverselist (self,head):
            prev=None
            while head:
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
            return prev
obj=linkedlist()
n=int(input("enter the value:"))
obj.createLL(n)
print("linked list")
obj.show(obj.head)
print("reverese linked list")
obj.head=obj.reverselist(obj.head)
obj.show(obj.head)


