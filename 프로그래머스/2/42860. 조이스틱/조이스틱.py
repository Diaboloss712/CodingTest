def solution(name):
    ans = 0
    pos = 0
    end = len(name) - 1
    
    for char in name:
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = pos + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        end = min(end, pos * 2 + len(name) - next)
        end = min(end, (len(name) - next) * 2 + pos)
        
        pos += 1
        
    return ans + end