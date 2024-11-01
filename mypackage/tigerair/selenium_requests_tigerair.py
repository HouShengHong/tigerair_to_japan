__all__ = [
    'tigerair_webdriver',
]

from selenium import webdriver as _webdriver
from selenium.webdriver.common.keys import Keys as _Keys
from selenium.webdriver.common.by import By as _By
from selenium.webdriver.support.ui import WebDriverWait as _WebDriverWait
from selenium.webdriver.support import expected_conditions as _EC

import requests as _requests

import time as _time
import datetime as _datetime

from .xpath import tigerair_elem_xpath as _tigerair_elem_xpath
from .xpath import tigerair_area_option_xpath as tigerair_area_option_xpath

from .url import tigerair_url as _tigerair_url
from .currency import tigerair_currency as tigerair_currency

from ..judge import *

class tigerair_webdriver:
    """
        This class is built for graphQL's id 
    """
    def __init__ (
        self,
        driver: _webdriver.Chrome = None,
        graphQL_id: str = None,
        graphQL_current_currency: str = None,
        graphQL_current_date: _datetime.date = None,
    ) -> None:

        self.driver = driver if driver is not None else _webdriver.Chrome()
        self.graphQL_id = graphQL_id if graphQL_id is not None else None
        self.graphQL_current_currency = graphQL_current_currency if graphQL_current_currency is not None else tigerair_currency.TWD
        self.graphQL_current_date = graphQL_current_date if graphQL_current_date is not None else _datetime.date.today()
        if not judge_datetime.type_eq_date(self.graphQL_current_date):
            raise TypeError("'graphQL_current_date's type should be 'datetime.date'. ")
        if not judge_datetime.date_ge_today(self.graphQL_current_date):
            raise ValueError("'graphQL_current_date' should be greater eq than today. ")

    def _driver_reopen(self):
        """
            Reopen the browser
        """
        self.driver.quit()
        self.driver = _webdriver.Chrome()

    def _driver_get(self,url = _tigerair_url.index):
        """
            Loads a web page in the current browser session.

            :param url: Uses default value 'tigerair_url.index' because this help to crawl the tigerair's flights
        """
        self.driver.get(url)

    def _driver_close(self):
        """
            Closes the current window.
        """
        self.driver.close()

    def _driver_quit(self):
        """
            Closes the browser and shuts down the ChromiumDriver executable.
        """
        self.driver.quit()

    def _elem_find(self,xpath):
        """
            Find an element By xpath.

            :param xpath: element xpath
            :return: element
        """
        self.driver.find_element
        return _WebDriverWait(self.driver, 10).until(
            _EC.presence_of_element_located((_By.XPATH, xpath))
        )
    
    def _elem_click(self,xpath) -> None:
        """
            Click an element By xpath.

            :param xpath: element xpath
        """
        elem = self._elem_find(xpath)
        elem.click()
        _time.sleep(0.5)
    
    def _elem_input(self,xpath,text) -> None:
        """
            Types into element By xpath.

            :param xpath: element's xpath
        """
        elem = self._elem_find(xpath)
        elem.send_keys(text)
        elem.send_keys(_Keys.RETURN)
        _time.sleep(0.5)

    def _local_storage_keys_value_get(self,local_storage_key:str = 'searchLogs') -> str:
        """
            Gets the local storage key's value in the current window.

            :param local_storage_key: uses default value 'searchLogs' because this local storage key includes "graphQL_id" that is necessary for crawling flights
            :return: the local storage key's value
        """
        return self.driver.execute_script(f'return window.localStorage.getItem("{local_storage_key}");')
    
    def _graphQL_id_analyze(self,value:str = None) -> str:
        """
            Analyzes 'graphQL_id' from the local storage key 'searchLogs's value

            :param value: The local storage key's value. You can get the value from the method 'self._local_storage_keys_value_get()'
            :return: graphQL id
        """
        value = value if value is not None else self._local_storage_keys_value_get()
        value = value[value.find("|"):]
        value = value[value.find("id") + 5:]
        return  value[:value.find('"')]

    def _graphQL_id_update(self) -> str:
        """
            Update self.graphQL_id By self._graphQL_id_analyze()

            :return: self.graphQL_id
        """
        self.graphQL_id = self._graphQL_id_analyze()
        return self.graphQL_id

    def graphQL_id_get(self) -> str:
        """
            Gets graphQL_id

            :return: graphQL_id
        """
        return self.graphQL_id
    
    def standard_init(self,
            destination_xpath:str = None,
            departure_date:_datetime.date = None,
            ) -> str:
        """
            Standardly initializes this class, and gets the most important value 'graphQL_id' that help to crawl the tigerair web. 

            :parma destination_xpath: Input the area's xpath where you want to go to.
                :default: tigerair_area_option_xpath.kanto
                :example: 
                    tigerair_area_option_xpath.kansai_and_shikoku    # <Recommended Usage> input the value by the class 'tigerair_area_option_xpath's attribute
                    '/html/body/div[6]/div/div/div/div[6]/button'    # directly input
            :parma departure_date: Inputs the date that you start the journey. Or you can just input today because you can change the date by "mypackage.requests_ticket" 
                :restrictions: 
                    Type(departure_date) should be 'datetime.date'.
                    'departure_date' should be today or later.
                :default: datetime.date.today()
                :example: datetime.date(year = 2024 , month = 6 , day = 21)
        """
        destination_xpath = destination_xpath if destination_xpath is not None else tigerair_area_option_xpath.kanto
        departure_date = departure_date if departure_date is not None else _datetime.date.today()
        


        if type(departure_date) != _datetime.date:
            raise TypeError("'departure_date's type should be 'datetime.date' ")

        if departure_date < _datetime.date.today():
            raise ValueError("'departure_date' should be today or later ")

        self._driver_get()

        self._elem_click(_tigerair_elem_xpath.language_bar)
        self._elem_click(_tigerair_elem_xpath.language_bar_option_chinese)

        self._elem_click(_tigerair_elem_xpath.language_bar)
        self._elem_click(_tigerair_elem_xpath.language_bar_option_chinese)

        self._elem_click(_tigerair_elem_xpath.currency_bar)
        self._elem_click(_tigerair_elem_xpath.currency_bar_option_TWD)

        self._elem_click(_tigerair_elem_xpath.round_trip)

        self._elem_click(_tigerair_elem_xpath.origin_airport_bar)
        self._elem_click(_tigerair_elem_xpath.origin_airport_bar_option_TPE)

        self._elem_click(_tigerair_elem_xpath.destination_airport_bar)
        self._elem_click(destination_xpath)

        self._elem_input(_tigerair_elem_xpath.departure_date_bar,departure_date.strftime("%Y%m%d"))
        self._elem_input(_tigerair_elem_xpath.return_date_bar,departure_date.strftime("%Y%m%d"))

        self._elem_click(_tigerair_elem_xpath.search)
        _time.sleep(5)
        return self._graphQL_id_update()

    def graphQL_currency_change(self, currency_usage:str = None):
        # default arg 
        currency_usage = currency_usage if currency_usage is not None else tigerair_currency.TWD

        # type check 'currency_usage'
        if type(currency_usage) != str :
            raise TypeError("'currency_usage's type should be 'str'. ")

        response_currency_change = _requests.post(url=_tigerair_url.graphQL,json=
            {
                "operationName": "appUpdateFlightSearchSession",
                "variables": {
                    "input": {
                    "id": f"{self.graphQL_id}",
                    "userCurrency": f"{currency_usage}"
                    }
                },
                "query": "mutation appUpdateFlightSearchSession($input: UpdateFlightSearchSessionInput!) {\n  appUpdateFlightSearchSession(input: $input) {\n    userCurrency\n  }\n}\n"
            }
        )
        self.graphQL_current_currency = currency_usage
        return response_currency_change

    
    def graphQL_date_change(self,date:_datetime.date):
        
        if not judge_datetime.type_eq_date(date):
            raise TypeError("'Arg:date's type should be equal 'datetime.date'. ")
        if not judge_datetime.date_ge_today(date):
            raise ValueError("'Arg:date's value should be greater than or equal to 'today'. ")

        response_date_change = _requests.post(url=_tigerair_url.graphQL,json = 
            {
                "operationName": "appUpdateFlightSearchSessionSearchDate",
                "variables": {
                    "input": {
                    "id": f"{self.graphQL_id}",
                    "departureDate": f"{date.strftime('%Y-%m-%d')}",
                    "returnDate": f"{date.strftime('%Y-%m-%d')}"
                    }
                },
                "query": "fragment UpdateSearchCondition on FlightSearchSession {\n  id\n  adultCount\n  childCount\n  infantCount\n  departureDate\n  returnDate\n  promotionCode\n  stationPairs {\n    origin\n    destination\n  }\n  userCurrency\n  pricingCurrency\n  flightType\n  expiredAt\n  portal {\n    slug\n    type\n    startAt\n    endAt\n    departStartAt\n    departEndAt\n    returnStartAt\n    returnEndAt\n    flightType\n    maxPassengerCount\n    defaultPromotionCode\n    promotionCodeLength\n    isPromotionCodeDisplayed\n    voucherDetail {\n      totalLength\n      discardStartLength\n      discardEndLength\n    }\n    creditCardDetail {\n      length\n      binCode\n    }\n    portalEmbargoDates {\n      startAt\n      endAt\n    }\n  }\n}\n\nmutation appUpdateFlightSearchSessionSearchDate($input: UpdateFlightSearchSessionSearchDateInput) {\n  appUpdateFlightSearchSessionSearchDate(input: $input) {\n    ...UpdateSearchCondition\n  }\n}\n"
            }
        )
        self.graphQL_current_date = date
        return response_date_change
    
    def graphQL_search_result(self):
        responese_search_result = _requests.post(url=_tigerair_url.graphQL ,json={
            "operationName": "appFlightSearchResult",
            "variables": 
            {
                "id": f"{self.graphQL_id}"
            },
            "query": "query appFlightSearchResult($id: String!) {\n  appFlightSearchResult(id: $id) {\n    id\n    sessionId\n    flightType\n    journeys {\n      legs {\n        origin\n        destination\n        departureDate\n        availabilityLegs {\n          origin\n          destination\n          legSellKey\n          duration\n          overnight\n          infantSoldOut\n          infantTooMany\n          availabilitySegments {\n            origin\n            destination\n            departureTime\n            arrivalTime\n            duration\n            overnight\n            carrierCode\n            flightNumber\n            availabilitySegmentDetails {\n              equipmentType\n              totalSeat\n              soldSeat\n              remainingSeat\n              subjectToGovernmentApproval\n              availabilitySegmentDetailSsrs {\n                ssrNestCode\n                ssrLid\n                ssrSold\n                ssrValueSold\n              }\n            }\n          }\n          fares {\n            sellable\n            availableCount\n            productClass\n            carrierCode\n            ruleNumber\n            fareSellKey\n            paxFares {\n              paxType\n              ticketPrice {\n                userCurrency\n                fareAmount\n                taxAmount\n                productClassAmount\n                promotionDiscountAmount\n                discountedFareAmount\n                totalAmountWithoutTax\n                discountedTotalAmountWithoutTax\n                totalAmount\n                discountedTotalAmount\n              }\n            }\n            fareLabels {\n              translations {\n                locale\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"
        })

        return responese_search_result

 # ______________________________________________________

    def destination_change_and_new_graphQL_id_update(self,destination):
        self._elem_click("/html/body/div[1]/div/div[1]/header/div[2]/div[2]/div/button[1]/span[2]/div/div")
        _time.sleep(0.5)
        self._elem_click("/html/body/div[6]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[2]/div/div/div/div[1]/input")
        _time.sleep(0.5)
        self._elem_click(destination)
        _time.sleep(0.5)
        self._elem_click("/html/body/div[6]/div/div[2]/div/div/div/form/div/div[3]/div[3]/button")
        _time.sleep(2)
        self._elem_click("/html/body/div[7]/div/div[2]/div/div[4]/button[2]")
        _time.sleep(5)
        self._graphQL_id_update()


    





