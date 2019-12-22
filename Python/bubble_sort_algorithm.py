from random import randint

#new_list = [100, randint(1, 1000), randint(1, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000) ,randint(0, 1000), randint(0, 1000)]

#print(str(new_list) + '\n')
def sort(new_list, a=0):
        while  len(new_list) > a:
                for i in range(len(new_list)-1):
                    if new_list[i] > new_list[i+1]:
                        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
                        print(new_list)
                a+=1
