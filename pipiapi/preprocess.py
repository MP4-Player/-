from collections import Counter
import collections

def preprocessing(words):
   vvod=(' '.join(map(str, words)))
   vvod=vvod.replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ')
   print(vvod)
   dlin= str(vvod).split()
   s=max(dlin, key=len)
   chasto = vvod.split() 
   Countered = Counter(chasto )   
   chastovst = Countered.most_common(1)
   return [s,chastovst[0][0]]

#from collections import Counter
#import collections

#def preprocessing(words):

    #counter = collections.Counter(words)
    #most_common, frequency = counter.most_common()[0]
    #longest = max(words, key=len)
    #often = str(most_common)
    #max_len = str(longest)
    #return [often, max_len]
    #vvod=str(words)
    #vvod=vvod.replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ')
    #print(vvod)
    #dlin= str(vvod).split()
    #s=max(dlin, key=len)
    #print('самое длинное',s)
     
  

    #chasto = vvod.split() 
    #Countered = Counter(chasto )   
    #chastovst = Countered.most_common(1)
    #print('самое chastoe',chastovst[0][0])
    #return [s,chastovst[0][0]]
#print('yjdjt')