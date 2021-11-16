
time1 = input('entet time:').split(':')
time2 = input('entet time:').split(':')
def time_display(a,b):
   hour=int(a[0])+int(b[0])
   minute=int(a[1])+int(b[1])
   if minute>=60:
       minute=minute%60
       hour+=1
   second=int(a[2])+int(b[2])
   if second>=60:
       second=second%60
       minute+=1
   print('time is' ,hour, 'hour(s) and ',minute,'minute(s) and',second,'second(s)')
time_display(time1,time2)





