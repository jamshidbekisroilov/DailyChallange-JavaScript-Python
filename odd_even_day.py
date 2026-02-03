from datetime import datetime, timezone
def odd_or_even_day(timestamp):
    date_object = datetime.fromtimestamp(timestamp / 1000, tz = timezone.utc)
    day = date_object.day
    print(day)
    return 'odd' if day % 2 != 0 else 'even'
#Demo test !!!Eslatma bu UTC 0 dagi time zona ishlatilgan 
print(odd_or_even_day(6739456780000))#Output: odd
print(odd_or_even_day(86400000))#Output: even
