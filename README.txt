Alpahabet soup
=============

General algorithm complexity: 

-  In this case we visit all items in letters bowl (letters), for knowing how many of each possible characters are in bowl.
   This seems to be linear complexity O(l), where l is the number of bowl letters.

-  We iterate over message items and discount one in count of corresponding letters if found; when we try to reach an element in bowl stats present in 
   message but with zero occurences left, we know we failed. 
   That seems to be linear complexity O(m), where m is the number of message letters.
   Some authors say we must add complexity of accessing the stats which may be not constant (access to bowl stats, depending what is the chosen structure
   could be O(log(l)), if it is a hash with collisions. If it is not a hash with colissions, we can assume it is O(1), i.e., constant

 - So final complexity, in terms of m and l, coud b set as O(l+m), which may be considered linear, as m should not be bigger than l. If they were equal,
   complexity should be O(2l) or O(2m), which is linear too.

Speeding up:

-  For big n and l, it seems Numpy speeds up the process up to 30% (from 55 sec in some iterations of testsi no-numpy algorithm, to 40 sec numpy algorithm).
-  So, there are two functions, checkSoupNumpy and checkSoup that perform the same algorithm with and without optimization

Measuring complexity:

-  In order to make sure assumptions are correct, we can launch some iterations of tests with big_o package, which heuristically tries to determine
   underlying complexity.
   For non-numpy algorithm, the results show algorithm is linear. 
   When numpy is used, big_o says it seems to be polynomial (numpy may introduce some other subalgorithms that are also measured), but seems to be
   faster than non-numpy algorithm (something logical per se) for big numbers of m and l

Other considerations:

- What happens if l is much bigger than m? 
  There could be some strategies of partitioning the bowl with the hope that partitions may contain the message without the need of counting all
  elements in bowl. The worst case would be the same (have to visit full letters bowl and message letters), with complexity remaining the same.
  But on average, probably less calculations would be needed to drop a result in positive cases.

- Think, having a previous knowledge in sizes of bowls and messages, and distribution of message's items could give us more possibilities for finding
  better algorithms, but the so general way the problem has been stated does not give us much more room for alternatives.


Required python packages:

- These have to be installed via pip
numpy,secrets,big_o,timeit

- These are part of Python 3 standard libs
collections,datetime

Kind regards,
Manuel.


