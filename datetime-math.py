import datetime
import time

START_TIME_STRING = '1498653864.182'
END_TIME_STRING = '1498659062.028'

print("Starttime: " + START_TIME_STRING)
print("Endtime  : " + END_TIME_STRING)

START_TIME_FLOAT = float(START_TIME_STRING)
END_TIME_FLOAT = float(END_TIME_STRING)

print("Starttime float: " + str(START_TIME_FLOAT))
print("Endtime float  : " + str(END_TIME_FLOAT))

START_TIME_STRFTIME = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(START_TIME_FLOAT))
END_TIME_STRFTIME = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(END_TIME_FLOAT))

print("StarttimeString: " + START_TIME_STRFTIME)
print("EndtimeString  : " + END_TIME_STRFTIME)

START_TIME_DATETIME = datetime.datetime.fromtimestamp(START_TIME_FLOAT)
END_TIME_DATETIME = datetime.datetime.fromtimestamp(END_TIME_FLOAT)
DURATION = END_TIME_DATETIME - START_TIME_DATETIME
print("Flow took : " + str(DURATION))
# A timedelta value specifying the seconds attribute
DURATION.seconds
HOURS = DURATION.seconds // 3600
MINUTES = DURATION.seconds // 60
MY_MINUTES = MINUTES - 60
SECONDS = DURATION.seconds - (MINUTES * 60)
print('Flow took : %s Hours %s Minutes %s Seconds' % (HOURS, MY_MINUTES, SECONDS))






#print(DURATION.ctime)
