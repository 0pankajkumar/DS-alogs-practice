source = [4,3,2,1]
auxilary = []
destination = []

def tower(source, auxilary, destination):
    print(source, auxilary, destination)
    # Moving m-1 disks from source to auxilary
    # Without violating rules
    if len(source) == 0:
        return
    if len(auxilary) != 0 and len(source) != 0:
        if auxilary[-1] < source[-1]:
            p = source.pop()
            auxilary.append(p)
            tower(source, auxilary, destination)

    # Move top disk from source to destination
    if len(source) != 0:
        t = source.pop()
        destination.append(t)
        tower(source, auxilary, destination)


    # Move m-1 disks from auxilary to destination
    # Without violating rules
    if len(auxilary) != 0:
        t = auxilary.pop()
        destination.attend(t)
        tower(source, auxilary, destination)















def tower_wikipedia(n, source, destination, auxilary):
    if n > 0:
        # Moving m-1 disks from source to auxilary
        # Without violating rules
        tower_wikipedia(n-1, source, auxilary, destination)
        # Move top disk from source to destination
        destination.append(source.pop())
        print(source, auxilary, destination)

        # Move m-1 disks from auxilary to destination
        # Without violating rules
        tower_wikipedia(n-1, auxilary, destination, source)

print("calling hanoi")

tower_wikipedia(4, source, destination, auxilary)
