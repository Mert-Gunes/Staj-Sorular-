def FirstReverse(strParam):
  strParamReverse = list(range(len(strParam)))
  iterator = 0
  for character in strParam:
    strParamReverse[-1-iterator] = strParam[0+iterator]
    iterator = iterator + 1
  strParamReverse = ''.join(str(e) for e in strParamReverse)
  strParam = strParamReverse


  # code goes here
  return strParamReverse

# keep this function call here 
print(FirstReverse(input()))