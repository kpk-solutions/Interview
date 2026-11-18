'''input = [4, 1, 2, 7, 5, 3, 1] # +2 # -5

#[4, 1, 2, 7, 5, 3, 9]
sum_of = []
for i in range(len(input)):
  s = 0
  print(i, input[i])
  for j in range(i+2, len(input), 2):
    print(j, input[j])
    s=s+input[i]+input[j]
  sum_of.append(s)
print(max(sum_of))'''

a = [0, 1, 2, 7, 5, 3, 1]

def mazSum(a):
    p1 = 0
    p2 = 0
    for i in a:
        t = p2
        p2 = p1
        p1 = max(p1, i+t)
    return max(p1, p2)
print(max(mazSum(a[1:]), mazSum(a[:-1])))

















#
# input = [4, 1, 2, 7, 5, 3, 1]
#
# sub1 = input[:-1]
# prev2, prev1 = 0,0
# for x in sub1:
#     prev2, prev1 =  prev1, max(prev1, prev2 + x)
# max1 = prev1
#
# sub2 = input[1:]
# prev2, prev1 = 0,0
# for x in sub2:
#     prev2, prev1 =  prev1, max(prev1, prev2 + x)
# max2 = prev1
# print(max(max1, max2))