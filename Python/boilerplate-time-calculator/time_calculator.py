def add_time(start, duration,day=False):
    weeks={'monday':0,
          'tuesday':1,
          'wednesday':2,
          'thursday':3,
          'friday':4,
          'saturday':5,
          'sunday':6}
    weekname={0:'Monday',
          1:'Tuesday',
          2:'Wednesday',
          3:'Thursday',
          4:'Friday',
          5:'Saturday',
          6:'Sunday'}
    start=start.split(' ')
    start_time = start[0]
    am_or_pm = start[1]
    start_time=start_time.split(':')
    start_hr = int(start_time[0])
    start_min = int(start_time[1])
    duration=duration.split(':')
    dur_hr = int(duration[0])
    dur_min = int(duration[1])
    if am_or_pm=='PM':
      start_hr+=12
    #counting Time
    final_hr=0
    final_min=0
    days=0
    ispm=0
    final_hr=start_hr+dur_hr

    final_min=start_min+dur_min
    if final_min>60:
      final_hr+=1
      final_min-=60
    if final_min>0 and final_min<10:
      final_min='0'+str(final_min)

    if final_hr>24:
      days=final_hr//24
      final_hr=final_hr%24
      if final_hr>12:
        ispm=1
        final_hr-=12
      elif final_hr==0:
        final_hr=12
        ispm=0
    elif final_hr>12 and final_hr<24:
      final_hr-=12
      ispm=1
    elif final_hr==12:
      final_hr=12
      ispm=1
    if ispm:
      new_time=str(final_hr)+':'+str(final_min)+' PM'
    else:
      new_time=str(final_hr)+':'+str(final_min)+' AM'
    if day:
      newday=(weeks[day.lower()]+days)%7
      new_time+=', '+weekname[newday]
    if days==1:
      new_time+=' (next day)'
    elif days>1:
      new_time+=' ('+str(days)+' days later)'
    return new_time