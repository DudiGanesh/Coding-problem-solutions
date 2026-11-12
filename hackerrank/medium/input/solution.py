# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y=map(int,input().split())
expr=input()
k=eval(expr)
print(k == y)
