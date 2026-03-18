def solution(sizes):
    hmin = 0
    wmin = 0
    for w,h in sizes:
        if w < h:
            h, w = w, h
        if wmin <= w:
            wmin = w
        if hmin <= h:
            hmin = h
    return hmin*wmin