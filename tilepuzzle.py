# importing copy module
import copy

def pegpuzzle(start,goal):  
    list1 = []
    list2 = [start,list1]
    return reverse(statesearch(start,goal,[],list2))

def statesearch(unexplored,goal,path,list2=[]):
    if unexplored == []:
        return []    
    elif goal == list2:
        return cons(goal,path)
    elif goal == head(unexplored):
        return cons(goal,path)
    if len(path) > 40:
        return []
    else:  
        
        if list2 != []: 
            index = FindBlank(unexplored) 
            result = statesearch(generateNewStates(unexplored,index[0],index[1],path),
                             goal,
                             cons((unexplored), path))  
        else:  
            index = FindBlank(head(unexplored)) 
            result = statesearch(generateNewStates(head(unexplored),index[0],index[1],path),
                             goal,
                             cons(head(unexplored), path)) 
            
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored),
                               goal,
                               path)   
                               
def FindBlank(currState):
    #print(currState)
    index = []
    for i in range(0, len(currState) ):  
        for j in range(0, len(currState[i]) ): 
            if currState[i][j] == 0 : 
                index.append(i)
                index.append(j)
                return index 

def generateNewStates(currState,i,j,path = []): 
    idx_list = []
    list1 =MoveDown(currState,i,j)  
    list2 = MoveUp(currState,i,j)
    list3 = MoveLeft(currState,i,j)  
    list4 = MoveRight(currState,i,j) 
    list5 = [list1,list2,list3,list4] 
    for i in range(len(list5)): 
        if list5[i] == []: 
            idx_list.append(i)  
            continue
        for j in range(len(path)):
            if list5[i] == path[j]: 
                idx_list.append(i)    
    res = [ele for idx, ele in enumerate(list5) if idx not in idx_list] 
    #print(res)
    return res

def MoveDown(currState,i,j): 
    list1 =copy.deepcopy(currState)
    if (i< len(list1)) & (j < len(list1[i]))  & (i != len(list1) - 1): 
        list1[i][j], list1[i+1][j] = list1[i+1][j], list1[i][j]    
        return list1 
    else:
                return []

def MoveRight(currState,i,j):  
    list1 =copy.deepcopy(currState)
    if (i< len(list1)) & (j < len(list1[i]))  & (j != len(list1[i]) -1): 
        list1[i][j], list1[i][j+1] = list1[i][j+1], list1[i][j] 
        return list1 
    else:
                return []

def MoveLeft(currState,i,j): 
    list1 =copy.deepcopy(currState)
    if (i< len(list1)) & (j < len(list1[i]))  & (j != 0): 
        list1[i][j], list1[i][j-1] = list1[i][j-1], list1[i][j] 
        return list1 
    else:
                return []
    
def MoveUp(currState,i,j): 
    list1 =copy.deepcopy(currState)
    if (i< len(list1)) & (j < len(list1[i]))  & (i != 0): 
        list1[i][j], list1[i-1][j] = list1[i-1][j], list1[i][j]  
        return list1 
    else:
                return []
   
def head(lst): 
    return lst[0]
def tail(lst):
    return lst[1:] 
def reverse(st):
    return st[::-1]   
def cons(item,lst):
    return [item] + lst     
a = pegpuzzle([[2,8,3],[1,0,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])
#([[0,1,2],[3,4,5],[6,7,8]],[[8,7,6],[5,4,3],[2,1,0]])
print(a)

