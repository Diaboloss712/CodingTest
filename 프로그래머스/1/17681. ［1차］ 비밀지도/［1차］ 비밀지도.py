def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_num = bin(arr1[i] | arr2[i])[2:].zfill(n)
        bin_num = bin_num.replace('1','#')
        bin_num = bin_num.replace('0',' ')
        answer.append(bin_num)
    return answer