__all__ = [
    "type_eq_date",
    "date_eq_today",
    "date_gt_today",
    "date_ge_today",
]

import datetime as _datetime

def type_eq_date(obj) -> bool:
    if type(obj) == _datetime.date:
        return True
    else:
        return False

def date_eq_today(date: _datetime.date) -> bool:
    if date == _datetime.date.today():
        return True
    else:
        return False
    
def date_gt_today(date: _datetime.date) -> bool :
    if date > _datetime.date.today():
        return True
    else:
        return False
    
def date_ge_today(date: _datetime.date) -> bool :
    if date >= _datetime.date.today():
        return True
    else:
        return False
