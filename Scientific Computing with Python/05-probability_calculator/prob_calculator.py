# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**hatContent) -> None:
        self.hatContent = hatContent
        self.contents = []
        for key in self.hatContent:
            for i in range(self.hatContent[key]):
                self.contents.append(key)

    def __str__(self) -> str:
        print(self.hatContent)

    def draw(self, number):
        ret = []
        if number >= len(self.contents):
            for i in range(len(self.contents)):
                choice = random.randrange(len(self.contents))
                ret.append(self.contents.pop(choice))      
        else:
            for i in range(number):
                choice = random.randrange(len(self.contents))
                ret.append(self.contents.pop(choice)) 
        return ret

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    
    for i in range(num_experiments):
        extHat = copy.deepcopy(hat)
        items = extHat.draw(num_balls_drawn)
        result = dict()
        for item in items:
            if item in result:
                result[item] += 1
            else:   
                result[item] = 1
        loopMatch = True
        
        for item in expected_balls:
            if item in result:
                if result[item] >= expected_balls[item]:
                    continue
                else:
                    loopMatch = False
                    break
            else:
                loopMatch = False
                break
        
        if loopMatch == True:
            matches += 1
            loopMatch == False
            

    return matches / num_experiments





