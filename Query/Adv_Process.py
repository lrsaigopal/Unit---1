import types
def Get_Type(c):#get type of operation to be performed for where clause
        if c == '>' :
                return 1
        elif c == '<' :
                return 2
        elif c == '=' :
                return 3
        elif c == '>=' :
                return 4
        elif c == '<=' :
                return 5
        elif c == '!=' :
                return 6



def Proc_Que(s, a, DB):#process the entered query
    j = 1  # no of items to be print
    r = s[-1]  # last value
    c = Get_Type(s[-2])  # type ie > etc 
    q = 1  # no of items to be checked
    return Select_From_DB(s, a, c, j, q, r, DB)
    
    

def gr(a, b):#comaprison for greater than
   
    a = int(a)
    b = int(b)
    if a > b :       
            return 1
    else :
            return 0

def less(a, b):#comaprison for lesser than
    a = int(a)
    b = int(b)
    if a < b :
        return 1
    else :
        return 0

def eq(a, b):#comaprison for equal to
    if type(a) == types.IntType :
        b = int(b)
        if a == b :
            return 1
        else :
            return 0
    else:
        if a == b :
            return 1
        else :
            return 0
        
def greq(a, b):#comaprison for greater than equal to
    a = int(a)
    b = int(b)
    if a >= b :
        return 1
    else :
        return 0

def leq(a, b):#comaprison for less than equal to
    a = int(a)
    b = int(b)
    if a <= b :
        return 1
    else :
        return 0
def neq(a, b):#comaprison for not equal to
    if type(a) == types.IntType :
        b = int(b)
        if a != b :
            return 1
        else :
            return 0
    else:
        if a != b :
            return 1
        else :
            return 0


def Select_From_DB(s, a, c, j, q, r, DB):#performs the processing of query;removes all failed cases
    failed = []
    for x in DB :
        true = 1
        if c == 1:
            true = gr(x[s[-q - 2]], r)                                
            
        elif c == 2:
            true = less(x[s[-q - 2]], r)
                
        elif c == 3:
            true = eq(x[s[-q - 2]], r)
                
        elif c == 4:
            true = greq(x[s[-q - 2]], r)
                
        elif c == 5:
            true = leq(x[s[-q - 2]], r)
                
        elif c == 6:
            true = neq(x[s[-q - 2]], r)
            
        if true == 0  :
            failed.append(x["Company_Name"])
    return failed

def Get_Query(a,DB):#get the query from user
    s = a.split()
    return Proc_Que(s, a, DB) 
