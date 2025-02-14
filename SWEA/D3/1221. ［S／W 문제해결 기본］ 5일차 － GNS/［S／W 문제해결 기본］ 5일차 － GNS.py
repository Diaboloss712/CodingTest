T = int(input())
for test_case in range(1, T+1):
    count = 0
    useless_data = input()
    dictionary = {'ZRO':0, "ONE":0, 'TWO':0, 'THR':0, 'FOR':0,
                  'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0
                  }
    print(f'#{test_case}')
    for char in input().split():
        dictionary[char] = dictionary.get(char)+1
    for data in dictionary:
        for i in range(dictionary[data]):
            print(data, end=" ")
