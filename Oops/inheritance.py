class myVillage :
    isTemple = True
    def getVillageName(str):
        return "Amar Pura Jalu Khaat"
    
class myHomeTown (myVillage) :
    def getHomeTownName(str):
        return "Nohar"
    
homeTown = myHomeTown()
print(homeTown.getHomeTownName())
print(homeTown.getVillageName())
if homeTown.isTemple:
    print("Le, aa k baat krdi bhaiji")
else:
    print("kyu maatho maaro bhaiji")
