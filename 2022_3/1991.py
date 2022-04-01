import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [ [] for _ in range(N) ]
for i in range(N):
    temp = list(sys.stdin.readline().split())
    graph[ord(temp[0])-65] += temp[1:]

def func1(C):
    sys.stdout.write(C)
    if graph[ord(C)-65][0] != ".":
        func1(graph[ord(C)-65][0])
    if graph[ord(C)-65][1] != ".":
        func1(graph[ord(C)-65][1])

def func2(C):
    if graph[ord(C)-65][0] != ".":
        func2(graph[ord(C)-65][0])
    sys.stdout.write(C)
    if graph[ord(C)-65][1] != ".":
        func2(graph[ord(C)-65][1])

def func3(C):
    if graph[ord(C)-65][0] != ".":
        func3(graph[ord(C)-65][0])
    if graph[ord(C)-65][1] != ".":
        func3(graph[ord(C)-65][1])
    sys.stdout.write(C)
func1("A")
print()
func2("A")
print()
func3("A")