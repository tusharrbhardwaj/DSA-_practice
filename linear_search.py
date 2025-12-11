class linear:
    
    def __init__(self,ls,target):
        self.ls = ls
        self.target = target

    
    def linear_search(self):
        '''
        Returtn the index postion of the target if found else returns None
        '''
        for i in range(0,len(self.ls)):
            if self.ls[i]== self.target:
                return i
        return None


    def verify(self,i):
        if i is not None:
            print(f"Traget found at index : {i}")
        else:
            print("Target Not Found")
    
def main(ls,target):
    search = linear(ls,target)
    index = search.linear_search()
    search.verify(index)
    
    
if __name__ == "__main__":
    ls = range(1,11)
    target = 9
    main(ls,target)

