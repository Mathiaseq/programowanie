class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def is_empty(self):
        return len(self.__stack_list) == 0

x=[]
while True:
    nazwisko=input("Podaj nazwisko: ")
    if nazwisko=="":
        break
    x.append(nazwisko)

stack_object = Stack()

for item in x:
    stack_object.push(item) 

while not stack_object.is_empty():
    print(stack_object.pop())
