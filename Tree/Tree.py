from collections import deque
from collections import defaultdict
class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.left=left
        self.data=data
        self.right=right


def buildtree(inputString):
    if(inputString=="" or inputString[0]=="null"):
        return None
    
    queue=deque()
    queue.append(Node(int(inputString[0])))
    root=queue[0]
    i=1
    while(queue):
    
        curr_node=queue.popleft()

        # left child

        if(inputString[i]!="null"):
            curr_node.left=Node(int(inputString[i]))
            i+=1
            queue.append(curr_node.left)
        else:
            i+=1
        

        # right child
        if(inputString[i]!="null"):
            curr_node.right=Node(int(inputString[i]))
            i+=1
            queue.append(curr_node.right)
        else:
            i+=1

        if(i>=len(inputString)):
            break

    return root



# Code starts here
    




if __name__ == "__main__":
    t=int(input())
    stringarr = list(map(str,input().split()))
    root=buildtree(stringarr)
    ans=verticalorder(root)
    for i in ans:
        print(i,end=" ")




