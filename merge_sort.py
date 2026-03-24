class sorting:
    '''
    Sorts a list in ascending order
    Returns a new sorted list
        
    Divid : find the mid point of list and divides list into sublist
    Conquer : Recursively sorts the sublists created in previous steps
    Combine : Merged the sorted sublists created in previous steps
    '''
    
    def __init__(self,ls):
        self.ls = ls
        
    def merge_sort(self,part_1,part_2):
        '''
        Merges two lists or arryas, sorting them in the process
        it retruns a sorted array
        '''
        def intializing(self):
            
            if len(self.ls) <= 1:
                return self.ls
            
            part_1, part_2 = self.split(self.ls)
            left = self.merge_sort(part_1)
            right = self.merge_sort(part_2)
            
            return self.merge(left,right)
        
        
        def split(self):
            '''
            Divide the unsorted list from midpoint into sublist.
            returns two sublists part_1 and part_2
            '''
            mid = len(self.ls)//2
            part_1 = self.ls[:mid]
            part_2 = self.ls[mid:]
            
            return part_1, part_2
    
    
        l = [] 
        i = 0
        j = 0
        
        while i < len(part_1) and j < len(part_2):
            if part_1[i] < part_2[j]:
                l.append(part_1[i])
                i+=1
            else :
                l.append(part_2[j])
                j+=1
                
        while i < len(part_1):
            l.append(part_1[i])
            i+=1
            
        while j < len(part_2):
            l.append(part_2[j])
            j+=1
            
        return l
     
            
    

    
    
            
listt = [54,62,93,17,77,31,44,55,20]


