from business_calendar import Calendar, MO, TU, WE, TH, FR
import datetime
date1 = datetime.datetime(2013,1,10)

# normal calendar, no holidays
cal = Calendar()
date2 = cal.addbusdays(date1, 25)
print('%s days between %s and %s' % \
    (cal.busdaycount(date1, date2), date1, date2))