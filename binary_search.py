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
        
def main(ls,target):
    search = binary(ls,target)
    index = search.binary_search()
    search.verify(index)
    
    
if __name__ == "__main__":
    ls = range(1,11)
    target = 4
    main(ls,target)
    