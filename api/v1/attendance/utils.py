"""
function for getting daily attendance details
#- working hours 
#- missing hours 
"""

# Daily query
def get_daily_attendance_sum(queryset):
    daily_wrk_hrs = {}
    base_working_hours = 10
    for i in queryset:
        day = i.check_in_time.date()
        day_query = queryset.filter(check_in_time__date=day)
        day_woking_hours = 0
        for j in day_query:
            day_woking_hours += j.working_hours
        new_dic = {
            "date": day,
            "working_hours": day_woking_hours,
            "missing_hours": (base_working_hours - day_woking_hours),
        }
        daily_wrk_hrs[str(day)] = new_dic
    return daily_wrk_hrs
