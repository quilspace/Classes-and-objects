
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
        self.new_name = new_name
        print(new_name)

    def change_age(self, new_age):
        self.new_age = int(new_age)
        print(new_age)
    
    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(self.tracks)

    def get_score(self):
        print(self.score)        




Bob = Student("Bob", 26, ["FE","BE"], 20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
