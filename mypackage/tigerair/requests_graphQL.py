"""

import requests as _requests 
import datetime as _datetime
from currency import *

from flight import flight as _flight 





def graphQL_date_change(graphQL_id:str,date:_datetime.date):
    response_date_change = _requests.post("https://api-book.tigerairtw.com/graphql",json = 
    {
    "operationName": "appUpdateFlightSearchSessionSearchDate",
    "variables": {
        "input": {
        "id": f"{graphQL_id}",
        "departureDate": f"{date.strftime('%Y-%m-%d')}",
        "returnDate": f"{date.strftime('%Y-%m-%d')}"
        }
    },
    "query": "fragment UpdateSearchCondition on FlightSearchSession {\n  id\n  adultCount\n  childCount\n  infantCount\n  departureDate\n  returnDate\n  promotionCode\n  stationPairs {\n    origin\n    destination\n  }\n  userCurrency\n  pricingCurrency\n  flightType\n  expiredAt\n  portal {\n    slug\n    type\n    startAt\n    endAt\n    departStartAt\n    departEndAt\n    returnStartAt\n    returnEndAt\n    flightType\n    maxPassengerCount\n    defaultPromotionCode\n    promotionCodeLength\n    isPromotionCodeDisplayed\n    voucherDetail {\n      totalLength\n      discardStartLength\n      discardEndLength\n    }\n    creditCardDetail {\n      length\n      binCode\n    }\n    portalEmbargoDates {\n      startAt\n      endAt\n    }\n  }\n}\n\nmutation appUpdateFlightSearchSessionSearchDate($input: UpdateFlightSearchSessionSearchDateInput) {\n  appUpdateFlightSearchSessionSearchDate(input: $input) {\n    ...UpdateSearchCondition\n  }\n}\n"
    })
    return response_date_change

#------------------------------------------------------

def graphQL_currency_change(graphQL_id:str = None , currency_usage:str = None):

    # default arg 
    graphQL_id = graphQL_id if graphQL_id is not None else None
    currency_usage = currency_usage if currency_usage is not None else tigerair_currency.TWD
    
    # type check 'graphQL_id'
    if type(graphQL_id) != str :
        raise TypeError("'graphQL_id's type should be 'str'. ")

    # type check 'currency_usage'
    if type(currency_usage) != str :
        raise TypeError("'currency_usage's type should be 'str'. ")

    response_currency_change = _requests.post(url='https://api-book.tigerairtw.com/graphql',json=
        {
            "operationName": "appUpdateFlightSearchSession",
            "variables": {
                "input": {
                "id": f"{graphQL_id}",
                "userCurrency": f"{currency_usage}"
                }
            },
            "query": "mutation appUpdateFlightSearchSession($input: UpdateFlightSearchSessionInput!) {\n  appUpdateFlightSearchSession(input: $input) {\n    userCurrency\n  }\n}\n"
        }
    )
    return response_currency_change







"""