def arithmetic_arranger(problems,args=False):
  firstline=''
  secondline=''
  thirdline=''
  forthline=''
  num_of_prob=len(problems)
  if num_of_prob>5:
      return "Error: Too many problems."
  for i in problems:
    substr=i.split()
    firstnum=substr[0]
    operators=substr[1]
    secondnum=substr[2]
    if operators!='+' and operators!='-':
      return "Error: Operator must be '+' or '-'."
    if len(firstnum)>4 or len(secondnum)>4:
      return "Error: Numbers cannot be more than four digits."
    if not firstnum.isdigit() or not secondnum.isdigit():
      return "Error: Numbers must only contain digits."
    sumoftwo=str(int(firstnum)+int(secondnum)) if operators=='+' else str(int(firstnum)-int(secondnum))
    linelength=max(len(firstnum),len(secondnum))+2
    topline=str(firstnum).rjust(linelength)
    secondnumline=operators+str(secondnum).rjust(linelength-1)
    dashline='-'*linelength
    ansline=sumoftwo.rjust(linelength)
    if i != problems[-1]:
      firstline+=topline+' '*4
      secondline+=secondnumline+ ' '*4
      thirdline+=dashline+' '*4
      forthline+=ansline+' '*4
    else:
      firstline+=topline
      secondline+=secondnumline
      thirdline+=dashline
      forthline+=ansline
  firstline.rstrip()
  secondline.rstrip()
  thirdline.rstrip()
  forthline.rstrip()
  if args:
    arranged_problems= firstline+'\n'+secondline+'\n'+thirdline+'\n'+forthline
  else:
    arranged_problems=firstline+'\n'+secondline+'\n'+thirdline
  return arranged_problems



"""
//Alternative Version---This actually works but fails to pass the test arrangement test, since I misunderstood the question requirements
from functools import reduce #python 3
import operator
def arithmetic_arranger(problems,args=False):
    num_of_prob=len(problems)
    addorsub=[]
    orglist=[]
    if num_of_prob>5:
      return "Error: Too many problems."
    else:
      #organizedlist=problems.replace(' + ',' ').replace(' - ',' ').split(' ')        
      for i in problems:
        if i.count(' + ')>0:
          addorsub.append(1)
          addorsub.append(1)
          orglist.append(i.split(' + '))
          #if not str(i.split(' + ')).isdigit():
            #return "Error: Numbers must only contain digits."
        elif i.count(' - ')>0:
          addorsub.append(0)
          addorsub.append(0)
          orglist.append(i.split(' - ')) 
          #if not str(i.split(' - ')).isdigit():
            #return "Error: Numbers must only contain digits."
        else:
          return "Error: Operator must be '+' or '-'."
      orglist=reduce(operator.concat,orglist)
      for i in orglist:
        if not i.isdigit():
          return "Error: Numbers must only contain digits."
      intlist=[int(x) for x in orglist]
      for i in intlist:
        if len(str(i))>4:
          return "Error: Numbers cannot be more than four digits."
      for i in range(0,num_of_prob*2-1,2):
        spacelen=max(len(str(intlist[i])),len(str(intlist[i+1])))+2
        firstlinespace=spacelen-len(str(intlist[i]))
        print(' '*firstlinespace+str(intlist[i]), end =' '*4)
      print('\n')
      for j in range(1,num_of_prob*2,2):
        spacelen=max(len(str(intlist[j])),len(str(intlist[j-1])))+2
        secondlinespace=spacelen-len(str(intlist[j]))-1
        if addorsub[j]==1:
          print('+'+' '*secondlinespace+str(intlist[j]), end =' '*4)
        elif addorsub[j]==0:
          print('-'+' '*secondlinespace+str(intlist[j]), end =' '*4)
      print('\n')
      for k in range(0,num_of_prob*2-1,2):
        spacelen=max(len(str(intlist[k])),len(str(intlist[k+1])))+2
        print('-'*spacelen, end =' '*4)
      print('\n')
      if args==True:
        for k in range(0,num_of_prob*2-1,2):
          spacelen=max(len(str(intlist[k])),len(str(intlist[k+1])))+2
          ans=intlist[k]+intlist[k+1]
          anslenspace=spacelen-len(str(ans))
          print(' '*anslenspace+str(ans),end=' '*4)

"""