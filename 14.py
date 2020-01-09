import random
import math

### Euclidean distance calculator 
def dist_cal (x1, y1 ,x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 -y2)**2)
    
    return distance
### Random points generator
def create_random(n_val):
    point_list = []
    for x in range(n_val):
        x = random.randint(-10000,10000)
        y = random.randint(-10000,10000)
        
        point_list.append([x,y])
    return point_list

if __name__ == '__main__':
  inside = 0
  outside = 0
  n_val = int(input("\nEnter the number of points that will be generated: "))
  
  
  points = create_random(n_val)
  
  for i in points:
      if dist_cal(i[0],i[1], 0,0) <= 10000:
          inside = inside +1
  
  
  
  print ('%0.8f' % (4*inside / (n_val)))