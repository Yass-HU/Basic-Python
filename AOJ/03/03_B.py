num_list = []
num = 0
num_lst = []
num = 0

while True:
    num = int(input())
    if num == 0:
        break
    num_lst.append(num)

for i in range(len(num_lst)):
    print('Case {}: {}'.format(i+1, num_lst[i]))