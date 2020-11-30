import numpy as np

def calculate(list):
    if (len(list))<9:
      raise ValueError( "List must contain nine numbers.")
    else:
      a=np.reshape(list,(3,3))
      b=[np.mean(a,axis=0).tolist(),np.mean(a,axis=1).tolist(),np.mean(list)]
      c=[np.var(a,axis=0).tolist(),np.var(a,axis=1).tolist(),np.var(list)]
      d=[np.std(a,axis=0).tolist(),np.std(a,axis=1).tolist(),np.std(list)]
      e=[np.max(a,axis=0).tolist(),np.max(a,axis=1).tolist(),np.max(list)]
      f=[np.min(a,axis=0).tolist(),np.min(a,axis=1).tolist(),np.min(list)]
      g=[np.sum(a,axis=0).tolist(),np.sum(a,axis=1).tolist(),np.sum(list)]
      calculations={'mean':b,
                'variance':c,
                'standard deviation':d,
                'max':e,
                'min':f,
                'sum':g}
      return calculations