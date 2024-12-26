def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return 'A'
    if 80 <= score < 90:
        return 'B'
    if 70 <= score < 80:
        return 'C'
    if 60 <= score < 70:
        return 'D'
    if 0 <= score < 60:
        return 'F'


print(get_grade(95, 90, 93))
