#Earliest-Start-Time-First Algorithm

class greedy_algo:
    
    def __init__(self,classes):
        self.classes = classes
        
    def sort_lecture(self):
        timings = [] 
        for key,(start,end) in self.classes.items():
            lecture = (key,start,end)
            timings.append(lecture)
            
        
        sorted_list = sorted(timings,key=lambda x: x[0])
        
        
        return sorted_list
        
    
    def room_allotment(self,lectures):
        classroom = {}
        room = 0
        for time in lectures:
            assigned = False

            for room_num in classroom:
                if classroom[room_num]["end"] <= time[1]:
                    classroom[room_num]["lectures"].append([time[0],self.classes[time[0]]])
                    classroom[room_num]["end"] = time[2]
                    assigned = True
                    break
            if not assigned:
                room += 1
                classroom[room] = {"end" : time[2], "lectures" : [time[0],self.classes[time[0]]]}
                
        print(classroom)       
        for alloted_rooms in classroom:
            print(f"Room {alloted_rooms}: {classroom[alloted_rooms]['lectures']}")


classes = {
    'f': [13, 14.5],
    'a': [9, 10.5],
    'i': [15, 16.5],
    'b': [9, 12.5],
    'e': [11, 14],
    'h': [14, 16.5],
    'd': [11, 12.5],
    'j': [15, 16.5],
    'c': [9, 10.5],
    'g': [13, 14],
}





scheduled = greedy_algo(classes)
lectures = scheduled.sort_lecture()
scheduled.room_allotment(lectures)

