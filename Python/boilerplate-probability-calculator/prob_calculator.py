import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self, **balls):
    self.contents=[]
    for color, numbers in balls.items():
        temp=[color]*numbers
        self.contents.extend(temp)

  def draw(self,number):
    balls_drawn=[]
    if number>=len(self.contents):
      return self.contents
    #random shuffle to draw the ball(cannot use)
    """
    random.shuffle(self.contents)
    for i in range(number):
      balls_drawn.append(self.contents.pop())
    """
    #random choice method
    for i in range(number):
      ball_picked = random.choice(self.contents)
      balls_drawn.append(ball_picked)
      self.contents.pop(self.contents.index(ball_picked))
    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #the times we get the ball expected
  M=0
  expected=[]
  for color, numbers in expected_balls.items():
      temp=[color]*numbers
      expected.extend(temp)

  for i in range(num_experiments):
    hat_copy=copy.deepcopy(hat)
    actual_hat=hat_copy.draw(num_balls_drawn)
    result=False
    for ball in expected:
      if ball in actual_hat:
        actual_hat.remove(ball)
        result=True
      else:
        result=False
        break
    if result:
      M+=1
  return M/num_experiments