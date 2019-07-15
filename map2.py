def sqr(x): return x ** 2
names = ["sam", "john", "james"]
map(sqr, map(len,names))
print(list(map(sqr, map(len,names))))


