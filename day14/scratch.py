jem = "[[1],[2,3,4]]\n"

evaled = eval(jem.strip())
print(evaled)
print(type(evaled))

evaled.insert(evaled.index([1]), [17])
print(evaled)