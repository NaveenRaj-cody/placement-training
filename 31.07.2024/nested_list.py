if __name__ == '__main__':
    m=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        m.append([name,score])
    def sec_lowg(m):
        sec_low = sorted(set(score for name, score in m))
        minx=min(sec_low)
        while minx in sec_low:
            sec_low.remove(minx)
        miny=min(sec_low)
        sec_lows = sorted([name for name, score in m if score == miny])
        for student in sec_lows:
            print(student) 
    sec_lowg(m)
