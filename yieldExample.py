# comments Addedd
def cube(n):
    return n**3

def simplifiedCubeGenerator(n):
    generatedResults =[]
    currentN = 1
    while currentN<=n:
        generatedResults.append(cube(currentN))
        currentN+=1
    return generatedResults

def generateUsingYield(n):
    currentN = 1
    while currentN <=n:
        yield cube(currentN)
        currentN+=1

print(simplifiedCubeGenerator(5))
print([i for i in generateUsingYield(5)])
