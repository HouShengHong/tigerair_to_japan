__all__ = [
    'flight',
]



import datetime as _datetime

class flight:
    def __init__(
        self,
        legSellKey:str = None,
        origin:str = None,
        destination:str = None,
        departureTime:_datetime.datetime = None,
        arrivalTime:_datetime.datetime = None,
        remainingSeat:int = None,
        availableCount:int = None,
        totalAmount:int = None,
        discountedTotalAmount:int = None
    ):
        self.legSellKey             = legSellKey if legSellKey is not None else None
        self.origin                 = origin if origin is not None else None
        self.destination            = destination if destination is not None else None
        self.departureTime          = departureTime if departureTime is not None else None
        self.arrivalTime            = arrivalTime if arrivalTime is not None else None
        self.remainingSeat          = remainingSeat if remainingSeat is not None else None
        self.availableCount         = availableCount if availableCount is not None else None
        self.totalAmount            = totalAmount if totalAmount is not None else None    
        self.discountedTotalAmount  = discountedTotalAmount if discountedTotalAmount is not None else None

    def __lt__(self,other:"flight"):
        if self.discountedTotalAmount is not None and other.discountedTotalAmount is not None :
            if self.discountedTotalAmount < other.discountedTotalAmount:
                return True
            elif self.discountedTotalAmount == other.discountedTotalAmount:
                if self.departureTime < other.departureTime:
                    return True
        elif self.discountedTotalAmount is not None and other.discountedTotalAmount is None :
            return True
        elif self.discountedTotalAmount is None and other.discountedTotalAmount is None :
            if self.departureTime < other.departureTime:
                return True
    
    def __str__(self):
        return f'''legSellKey              : {self.legSellKey}
origin                  : {self.origin}
destination             : {self.destination}
departureTime           : {self.departureTime}
arrivalTime             : {self.arrivalTime}
remainingSeat           : {self.remainingSeat}
availableCount          : {self.availableCount}
totalAmount             : {self.totalAmount}
discountedTotalAmount   : {self.discountedTotalAmount}'''

    def _data_insert(self,origin_data:dict):
        self.legSellKey             = origin_data["legSellKey"]
        self.origin                 = origin_data["origin"]
        self.destination            = origin_data["destination"]
        self.departureTime          = _datetime.datetime.strptime(origin_data["availabilitySegments"][0]["departureTime"], "%Y-%m-%d %H:%M:%S")  
        self.arrivalTime            = _datetime.datetime.strptime(origin_data["availabilitySegments"][0]["arrivalTime"], "%Y-%m-%d %H:%M:%S")
        self.remainingSeat          = origin_data["availabilitySegments"][0]["availabilitySegmentDetails"][0]["remainingSeat"]
        if origin_data["fares"] != []:
            self.availableCount         = origin_data["fares"][0]["availableCount"]
            self.totalAmount            = origin_data["fares"][0]["paxFares"][0]["ticketPrice"]["totalAmount"]
            self.discountedTotalAmount  = origin_data["fares"][0]["paxFares"][0]["ticketPrice"]["discountedTotalAmount"]
        else:
            self.availableCount         = 0
            self.totalAmount            = None
            self.discountedTotalAmount  = None

    def data():
        pass


# class flights:
#     def __init__(
#         self,
#         webdriver:tigerair_webdriver = None,
#         flights:dict = None,

#     ):
#         self.webdriver = webdriver if webdriver is not None else tigerair_webdriver
#         self.flights = webdriver if webdriver is not None else {
            
#         }  

#         pass




# ____________________________________________________


# today = datetime.date(year=2024,month=8,day=1)

# lst_chubu_flights_to:list[flight] = []
# lst_chubu_flights_back:list[flight] = []

# lst_kanto_flights_to:list[flight] = []
# lst_kanto_flights_back:list[flight] = []




# for i in range(6):
#     mypackage.requests_tickets.date_change(chubu_graphQL_id,today + datetime.timedelta(days=i))
#     a = requests.post('https://api-book.tigerairtw.com/graphql',json={
#         "operationName": "appFlightSearchResult",
#         "variables": 
#         {
#             "id": f"{chubu_graphQL_id}"
#         },
#         "query": "query appFlightSearchResult($id: String!) {\n  appFlightSearchResult(id: $id) {\n    id\n    sessionId\n    flightType\n    journeys {\n      legs {\n        origin\n        destination\n        departureDate\n        availabilityLegs {\n          origin\n          destination\n          legSellKey\n          duration\n          overnight\n          infantSoldOut\n          infantTooMany\n          availabilitySegments {\n            origin\n            destination\n            departureTime\n            arrivalTime\n            duration\n            overnight\n            carrierCode\n            flightNumber\n            availabilitySegmentDetails {\n              equipmentType\n              totalSeat\n              soldSeat\n              remainingSeat\n              subjectToGovernmentApproval\n              availabilitySegmentDetailSsrs {\n                ssrNestCode\n                ssrLid\n                ssrSold\n                ssrValueSold\n              }\n            }\n          }\n          fares {\n            sellable\n            availableCount\n            productClass\n            carrierCode\n            ruleNumber\n            fareSellKey\n            paxFares {\n              paxType\n              ticketPrice {\n                userCurrency\n                fareAmount\n                taxAmount\n                productClassAmount\n                promotionDiscountAmount\n                discountedFareAmount\n                totalAmountWithoutTax\n                discountedTotalAmountWithoutTax\n                totalAmount\n                discountedTotalAmount\n              }\n            }\n            fareLabels {\n              translations {\n                locale\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"
#     })
#     to_trip   = a.json()["data"]["appFlightSearchResult"]["journeys"][0]["legs"][0]["availabilityLegs"]
#     back_trip = a.json()["data"]["appFlightSearchResult"]["journeys"][1]["legs"][0]["availabilityLegs"]
#     for i in to_trip :
#         flight_tmp = flight()
#         flight_tmp.data_insert(i)
#         lst_chubu_flights_to.append(flight_tmp)

#     for i in back_trip :
#         flight_tmp = flight()
#         flight_tmp.data_insert(i)
#         lst_chubu_flights_back.append(flight_tmp)

# for i in range(6):
#     mypackage.requests_tickets.date_change(kanto_graphQL_id,today + datetime.timedelta(days=i))
#     a = requests.post('https://api-book.tigerairtw.com/graphql',json={
#         "operationName": "appFlightSearchResult",
#         "variables": 
#         {
#             "id": f"{kanto_graphQL_id}"
#         },
#         "query": "query appFlightSearchResult($id: String!) {\n  appFlightSearchResult(id: $id) {\n    id\n    sessionId\n    flightType\n    journeys {\n      legs {\n        origin\n        destination\n        departureDate\n        availabilityLegs {\n          origin\n          destination\n          legSellKey\n          duration\n          overnight\n          infantSoldOut\n          infantTooMany\n          availabilitySegments {\n            origin\n            destination\n            departureTime\n            arrivalTime\n            duration\n            overnight\n            carrierCode\n            flightNumber\n            availabilitySegmentDetails {\n              equipmentType\n              totalSeat\n              soldSeat\n              remainingSeat\n              subjectToGovernmentApproval\n              availabilitySegmentDetailSsrs {\n                ssrNestCode\n                ssrLid\n                ssrSold\n                ssrValueSold\n              }\n            }\n          }\n          fares {\n            sellable\n            availableCount\n            productClass\n            carrierCode\n            ruleNumber\n            fareSellKey\n            paxFares {\n              paxType\n              ticketPrice {\n                userCurrency\n                fareAmount\n                taxAmount\n                productClassAmount\n                promotionDiscountAmount\n                discountedFareAmount\n                totalAmountWithoutTax\n                discountedTotalAmountWithoutTax\n                totalAmount\n                discountedTotalAmount\n              }\n            }\n            fareLabels {\n              translations {\n                locale\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"
#     })
#     to_trip   = a.json()["data"]["appFlightSearchResult"]["journeys"][0]["legs"][0]["availabilityLegs"]
#     back_trip = a.json()["data"]["appFlightSearchResult"]["journeys"][1]["legs"][0]["availabilityLegs"]
#     for i in to_trip :
#         flight_tmp = flight()
#         flight_tmp.data_insert(i)
#         lst_kanto_flights_to.append(flight_tmp)

#     for i in back_trip :
#         flight_tmp = flight()
#         flight_tmp.data_insert(i)
#         lst_kanto_flights_back.append(flight_tmp) 