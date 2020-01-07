
class item:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class stack:
    def __init__(self, top, height):
        self.top = top
        self.height = height
    def pussh(self, a):
        t = item(a, self.top)
        top = t
        self.height += 1
    def popp(self):
        t = top.value
        top = top.next
        self.height -= 1
    def iterate(self):
        for a in range(self.height):
            if a is not None:
                print(a, end=" ")
                print()

    # Inserting at bottom of stack
    # Although that's not a normal operation for stack
    # But it's recommended exercise from byte-by-byte for recursion

    # Not working properly

    def helper(self, curr, a):
        if curr.next is None:
            t = item(a, None)
            curr.next = t
        else:
            # bottom = curr
            self.helper(self, curr.next, a)

    def insertBottom(self, a):
        curr = self.top
        bottom = self.top
        self.helper(curr, a)


myStack = stack(None, 1)
for i in range(6):
    myStack.pussh(i)

myStack.insertBottom(67)

myStack.iterate()
