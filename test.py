distribution = {
  "GREEN": 10,
  "YELLOW": 5,
  "BROWN": 6,
  "BLUE": 30,
  "PINK": 5,
  "ORANGE": 9,
  "RED": 9,
  "WHITE": 12,
  "ARSH": 1,
  "BLACK": 1,
  "CREAM": 1,
  "BLEW": 1
}
values = sorted(list(distribution.values()))

def mean_color():
  """return the mean color"""
  mean = round(sum(values) / len(distribution)) #the mean of the distribution
  print('mean shirt is at', mean)

# to find the mode that is colour with the maximum frequency
def mode_val():
  for k, v in distribution.items():
    if distribution.get(k) == max(values):
      mode = k
      break
  print("Mostly worn shirt is", mode)

# probability of choosing a red shirt at random
def prob():
  prob = distribution.get('RED')/sum(values)
  print("probability of picking a RED shirt is", prob)

mean_color()
mode_val()
prob()