
# Linked list item
class item(object):
    """docstring for item."""

    def __init__(self, value, next):
        self.value = value
        self.next = next

e = item(5, None)
d = item(4, e)
c = item(3, d)
b = item(2, c)
a = item(1, b)

def iterateReverse(a):
    if a.next is None:
        return
    iterateReverse(a.next)
    print(a.value)

iterateReverse(a)
