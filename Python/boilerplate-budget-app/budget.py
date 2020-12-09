import operator
class Category:
  def __init__(self,name):
    self.name=name
    self.ledger=[]
    self.balance=float(0)
    self.spent=float(0)

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance+=amount
  
  def withdraw(self,amount,description=""):
    if not self.check_funds(amount):
      return False
    else:
      self.ledger.append({"amount": -amount, "description": description})
      self.balance-=amount
      self.spent+=amount
      return True
  
  def get_balance(self):
    return self.balance

  def transfer(self,amount_to_transfer,category_to_transfer):
    if not self.check_funds(amount_to_transfer):
      return False
    else:
      self.withdraw(amount_to_transfer,f"Transfer to {category_to_transfer.name}")
      category_to_transfer.deposit(amount_to_transfer,f"Transfer from {self.name}")
      return True

  def check_funds(self,amount):
    return self.balance>=amount

  def __str__(self):
    catg_name_len=len(self.name)
    title='*'*(15-catg_name_len//2)+self.name
    title+='*'*(30-len(title))
    content=""
    for item in self.ledger:
      description=item['description'][:23]
      amount="{:.2f}".format(item["amount"])[:7]
      spaces=" " * (30 - len(description) - len(amount))
      content+=description + spaces + amount + "\n"
    content+='Total: '+str(round(self.get_balance(),2))
    return title+'\n'+content

def get_eachcatvalue(differentcategories):
  #print(differentcategories)
  #sorted_cat = sorted(differentcategories, key=operator.attrgetter('spent'))
  #differentcategories=sorted(differentcategories, key=lambda x: x.spent,reverse=True)
  #differentcategories.sort(key=lambda x: x.spent,reverse=True)
  #print(differentcategories)
  names=[]
  spent=[]
  total_spent=0
  for cat in differentcategories:
    names.append(cat.name)
    spent.append(cat.spent)
    total_spent+=cat.spent
    #print(cat.name)
    #print(cat.spent)
  """
  dicts=dict(zip(names,spent))  
  sorted(dicts.items(), key=lambda x: x[1], reverse=True)
  names=dicts.keys()
  spent=dicts.values()
  """
  return names, spent, total_spent

def create_spend_chart(categories):
  names,spent,total_spent=get_eachcatvalue(categories)
  spent_percentage=[]
  for amount in spent:
    spent_percentage.append(int(amount/total_spent*100))
  bar_title = "Percentage spent by category\n"
  #create chart(y-axis)
  chart=""
  for i in range(100,-10,-10):
    sidespace=" "*(3-len(str(i)))
    chart+=f"{sidespace}{i}| "
    for bars in spent_percentage:
      if bars>=i:
        chart+="o  "
      else:
        chart+="   "
    chart+='\n'
  #create chart(x-axis)
  #dashline first
  chart+=" "*4 + '-' + '---'*len(spent_percentage)+ '\n'
  #vertical names
  sorted_names=sorted(names,key=len)
  for row in range(len(sorted_names[-1])):
    chart+=" "*5
    for name in names:
      if len(name)>row:
        chart+=name[row]+" "*2
      else:
        chart+=" "*3
    chart+='\n'
  return (bar_title+chart)[:-1]
