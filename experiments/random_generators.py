'''
Methods to generate:
    Random Numbers from min_val to max_val
    Random element from list
    K random elements within a given List
    Random string with given max and min length and allowed characters list

'''

from random import Random

rnd=Random()
rnd.seed(200)


def generate_number(min_val:int, max_val:int)->int:
    # number between max and min
    return rnd.randint(min_val,max_val)
 
def element_from_list(lst:list):
    # single random within a given list
    return rnd.choice(lst)

def elements_from_list(lst:list, weights=None, cum_weights=None, k=1):
    # K random within a given list with given weights
    return rnd.choices(lst, weights=weights, cum_weights=cum_weights, k=k)


def random_alphanum(min_len:int=1, max_len:int=10, from_list=None):
    '''
    min_len: minimum possible length of string, 1 by default
    max_len: max possible length of string, 10 by default
    from_list: random character from list, all aplphanumeric chars(unicode 0-225)
    ''' 
    strlen=generate_number(min_len, max_len)
    result=""
    if(from_list is None):
        from_list=[chr(i) for i in range(33,127)]
    for _ in range(0,strlen):
        char=element_from_list(from_list)
        result+=str(char)
    return result


# generate_number_between(10,10000)
# for _ in range(200):
#     print(elements_from_list(lst=["haathi","ghoda","beluga","hecker","sher"], k=3))

for _ in range(200):
    print(random_alphanum())


# generating codes from 
# with open("./sample_data/int_to_char.txt", "w+", encoding="utf-8") as f:
#     f.write(f"{'code'} \t\t{'char'} \n")
#     for i in range(0,2**16):
#         # print(f"{i} \t\t\t{chr(i)}\n")    
#         try:
#             f.write(f"{i} \t\t\t{chr(i)}\n")
#         except Exception:
#             pass
