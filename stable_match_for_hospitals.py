def matching(hospital_pref,student_pref):
    matching = {"Atlanta" : None, "Boston":None, "Chicago" : None}
    matched_hospitals = []
    matched_students = []
    
    pointer = 0
    while None in matching.values():
        hospital = matching.values().index(None)
        student = hospital_pref[hospital[pointer]]
        
        if student not in matched_students:
            matching[hospital] = student
            matched_students.append(student)
            matched_hospitals.append(hospital)
            
        elif student in matched_students:
            
            if student_pref[student].index(hospital) < matching.values().index(student):
                matching[hospital] = student
                
            else:
                pointer+=1
                   
        else:
            pointer+=1
            
            
    return matching
           
     
    
    
    

# This is hospital preferanec dictonary, which contains list of students that hospital prefer, low index --> high preference
hospital_pref = {
                'Atlanta' : ["Xaviour","Zeus","Yalando"],
                'Boston' : ["Yalando","Xaviour","Zeus"],
                'Chicago' : ["Xaviour","Zeus","Yalando"]
                }

# This is student preferanec dictonary, which contains list of hospital that students prefer, low index --> high preference
student_pref = { 
                'Xaviour' : ["Boston","Atlanta","Chicago"], 
                'Yalando' : ["Atlanta","Boston","Chicago"],
                "Zeus" : ["Chicago","Boston","Atlanta"]
                }

hospital = hospital_pref.keys()
student = student_pref.keys()


print(matching(hospital_pref,student_pref))