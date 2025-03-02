def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            answer = i
            return answer
    answer = len(citations)
    return answer