num_seg = int(input())

num_hr = num_seg//3600
resto = num_seg%3600
num_min = resto//60
num_seg_2 = resto%60
print('{:.0f}'.format(num_hr)+":"+'{:.0f}'.format(num_min)+":"+'{:.0f}'.format(num_seg_2))