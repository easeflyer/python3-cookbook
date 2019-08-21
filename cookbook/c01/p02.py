def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


scores = [0.1,1,2,3,4,5,6,7,8,9,10,99]

print(drop_first_last(scores))

# 33
print(33)