import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers")

  matrix = np.array(list).reshape((3, 3))

  # print(matrix)
  
  calculations = {}
  calculations['mean'] = [matrix.mean(axis=0), matrix.mean(axis=1), matrix.mean()]
  calculations['variance'] = [matrix.var(axis=0), matrix.var(axis=1), matrix.var()]
  calculations['standard deviation'] = [matrix.std(axis=0), matrix.std(axis=1), matrix.std()]
  calculations['max'] = [matrix.max(axis=0), matrix.max(axis=1), matrix.max()]
  calculations['min'] = [matrix.min(axis=0), matrix.min(axis=1), matrix.min()]
  calculations['sum'] = [matrix.sum(axis=0), matrix.sum(axis=1), matrix.sum()]
  
  # print(calculations)

  
  



  return calculations