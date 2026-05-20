def getTotalScore(s1, s2, s3):
    return s1 + s2 + s3

def getAverageScore(s1, s2, s3):
    return getTotalScore(s1, s2, s3) / 3

def getPassOrFail(s1, s2, s3):
    if getAverageScore(s1, s2, s3) >= 60:
        if s1 >= 40 and s2 >= 40 and s3 >= 40:
            return 'Pass'
    
    return 'Fail'