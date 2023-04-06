import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, balls):
    balls_choosen = []
    if balls > len(self.contents):
      return self.contents
    else:
      for i in range(balls):
        balls_choosen.append(self.contents.pop(random.randrange(len(self.contents))))
        
    return balls_choosen

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #Start some variables used in the experiment and populate a list of expected balls
  success = 0
  expected_balls_populated = []
  for key, value in expected_balls.items():
    for i in range(value):
      expected_balls_populated.append(key)
  
  #The experiment begins here:
  for i in range(num_experiments):
    #Copy the hat
    experiment_hat = copy.deepcopy(hat)
    #Copy the expected group of balls
    experiment_expected = copy.copy(expected_balls_populated)
    #Do the draws of balls from the hat
    drawn_balls = experiment_hat.draw(num_balls_drawn)
    
    #Check if the balls drawn from the hat are sufficient to the expected ones
    for element in drawn_balls:
      for i in range(len(experiment_expected)):
        if element == experiment_expected[i]:
          experiment_expected.pop(i)
          break
    #When all the balls from the expected group are being checked with drawn ones, it's a success
    if not experiment_expected:
      success += 1
        
  #Probability is calculated and returned
  probability = success / num_experiments

  return probability