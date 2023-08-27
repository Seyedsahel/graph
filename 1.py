n=int(input("inter the number of vertces:"))
print("enter the adhjacency matrix row by row , separated by spaces:")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("error : row should contain exactly {} integers".format(n))
        exit()
    adj_matrix.append(row)
edges = []
for i in range(n):
    for j in range (i+1,n):
        if adj_matrix[i][j]==1:
            edges.append((i,j))
G=Graph(edges)
print(adj_matrix)
G.show()
l=0
if G.is_connected():
    for i in range(n):
        for j in range(n):
            l=l+G.shortest_path_length(i,j) 
    print(l/2)
else:
    print("error : your graph is not connected")
# ........
from sage.graphs.connectivity import connected_components_subgraphs
from sage.graphs.connectivity import connected_components_number

P=Graph()
vertices = input('Enter vertices (Like: 1,2,3,4,5) : ').split(',')
T=int(input('Enter the number of edges (Like: 3) : '))
for v in vertices:
    P.add_vertex(v)
for counter in range(0,T):
    x,y=input('Enter an edge (Like: 1,2) : ').split(',')
    P.add_edge([x,y])
show(P)

o=0
L = connected_components_subgraphs(P)
graphs_list.show_graphs(L,vertex_labels=True,vertex_size=150)
Q = P.laplacian_matrix()
i=0
for e in Matrix(Q).eigenvalues():
    if e==0:
        i=i+1
if i==connected_components_number(P):
    print(i)
    print(connected_components_number(P))
# ........
count=0
for r in range(1,21):
    for Q in graphs.nauty_geng(r):
        if Q.is_regular(3):
            Graph=Q.plot()
            count=count+1
            Graph.save(f'{count}.png')
# ......
U=Graph()
vertices = input('Enter vertices separated by , : ').split(',')
n=0
for z in vertices:
    n=n+1
print(n)
T=int(input('Enter the number of edges: '))
for v in vertices:
    U.add_vertex(v)
for counter in range(0,T):
    x,y=input('Enter an edge like 1,2 and press enter: ').split(',')
    U.add_edge([x,y])
show(U)
M=U.spanning_trees_count()
print(M)
Q = U.laplacian_matrix()
i=1
z=0
for e in Matrix(Q).eigenvalues():
    if e!=0:
        i=e*i
        z=z+1
if z==0:
    i=0

print("number of Spanning trees: ",M)
print(i/n)
# .....
Q=Graph()
U=Graph()
vertices1 = input('Enter vertices separated by , : ').split(',')
T=int(input('Enter the number of edges: '))
for v in vertices1:
    U.add_vertex(v)
    Q.add_vertex(v)

for counter in range(0,T):
    x,y=input('Enter an edge like 1,2 and press enter: ').split(',')
    U.add_edge([x,y])
    Q.add_edge([x,y])
show(U)

W=Graph()
vertices2 = input('Enter vertices separated by , : ').split(',')
T=int(input('Enter the number of edges: '))
for v in vertices2:
    W.add_vertex(v)
    Q.add_vertex(v)
for counter in range(0,T):
    x,y=input('Enter an edge like 1,2 and press enter: ').split(',')
    W.add_edge([x,y])
    Q.add_edge([x,y])
show(W)

for e in vertices1:
    for r in vertices2:
        Q.add_edge([e,r])

show(Q)