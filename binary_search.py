class binary:
    
    def __init__(self,ls,target):
        self.ls = ls
        self.target = target
    
    def binary_search(self):
        '''
        Returtn the index postion of the target if found else returns None
        '''
        first = 0
        last = len(self.ls) - 1
        
        while first<=last:
            mid = (first+last)//2
            if self.ls[mid] == self.target:
                return mid
            elif self.ls[mid] < self.target:
                first = mid+1
            else:
                last = mid-1
            
        return None

    def verify(self,index):
        if index is not None:
            print(f"Traget found at index : {index}")
        else:
            print("Target Not Found")
  
  
class recursive_binary:
    
    def __init__(self,ls,target):
        self.ls = ls
        self.target = target
    
    def recurisive_binary_search(self):
        
        if len(self.ls) == 0:
            return False
        else:
            mid = (len(self.ls))//2
            
            if self.ls[mid] == self.target:
                return True
            else:
                if self.ls[mid] < self.target:
                    return recursive_binary(self.ls[mid+1:],self.target).recurisive_binary_search()
                else:
                    return recursive_binary(self.ls[:mid],self.target).recurisive_binary_search()
            
    
    def verify(self,result):
            print("Element Found",result)
 
 
  
        
def main(ls,target):
    search = binary(ls,target)
    index = search.binary_search()
    search.verify(index)
    search = recursive_binary(ls,target)
    result = search.recurisive_binary_search()
    search.verify(result)
    
    
if __name__ == "__main__":
    ls = range(1,11)
    target = 2
    main(ls,target)
    