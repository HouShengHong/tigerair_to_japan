__all__ = [
    "tigerair_elem_xpath",
    "tigerair_area_option_xpath",
]

class tigerair_elem_xpath:
    language_bar = '/html/body/div[1]/div/div/header/div/div[2]/button[2]'
    language_bar_option_chinese = '/html/body/div[6]/div/div/div[6]'

    currency_bar = '/html/body/div[1]/div/div/header/div/div[2]/button[3]/span[2]/div'
    currency_bar_option_TWD = '/html/body/div[6]/div/div/div[1]'

    round_trip = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[1]/div[1]/div[2]/div[1]/div[1]'

    origin_airport_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[1]/div/div'
    origin_airport_bar_option_TPE = '/html/body/div[6]/div/div/div/div[3]/button'

    destination_airport_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[2]/div/div'
    # destination_airport_bar_option_kanto = '/html/body/div[6]/div/div/div/div[2]/button'

    # It is input elem
    departure_date_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[2]/div/div/label[1]/div/div/div[1]/input'
    # It is input elem
    return_date_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[2]/div/div/label[2]/div/div/div[1]/input'

    search = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[3]/div[3]/button'

    @classmethod
    def method_all_attrs(cls):
        dic_attrs = {}
        for attr in cls.__dict__:
            if not attr.startswith('__') and not callable(getattr(cls, attr)):
                dic_attrs[attr] = getattr(cls, attr)
        return dic_attrs

class tigerair_area_option_xpath:
    kanto               = '/html/body/div[6]/div/div/div/div[2]/button'
    # NRT="/html/body/div[6]/div/div/div/div[3]/button"
    # HND="/html/body/div[6]/div/div/div/div[4]/button"
    # IBR="/html/body/div[6]/div/div/div/div[5]/button"

    kansai_and_shikoku  = '/html/body/div[6]/div/div/div/div[6]/button'
    # KIX="/html/body/div[6]/div/div/div/div[7]/button"
    # OKJ="/html/body/div[6]/div/div/div/div[8]/button"
    # KCZ="/html/body/div[6]/div/div/div/div[9]/button"

    kyushu              = '/html/body/div[6]/div/div/div/div[10]/button'
    # FUK="/html/body/div[6]/div/div/div/div[11]/button"
    # HSG="/html/body/div[6]/div/div/div/div[12]/button"
    # OKA="/html/body/div[6]/div/div/div/div[13]/button"
    
    chubu               = '/html/body/div[6]/div/div/div/div[14]/button'
    # NGO="/html/body/div[6]/div/div/div/div[15]/button"
    # KMQ="/html/body/div[6]/div/div/div/div[16]/button"
    # KIJ="/html/body/div[6]/div/div/div/div[17]/button"

    tohoku              = '/html/body/div[6]/div/div/div/div[18]/button'
    # SDJ="/html/body/div[6]/div/div/div/div[19]/button"
    # AXT="/html/body/div[6]/div/div/div/div[20]/button"
    # HNA="/html/body/div[6]/div/div/div/div[21]/button"
    # FKS="/html/body/div[6]/div/div/div/div[22]/button"

    hokkaido            = '/html/body/div[6]/div/div/div/div[23]/button'
    # HKD="/html/body/div[6]/div/div/div/div[24]/button"
    # CTS="/html/body/div[6]/div/div/div/div[25]/button"
    # AKJ="/html/body/div[6]/div/div/div/div[26]/button"

    @classmethod
    def method_all_attrs(cls):
        dic_attrs = {}
        for attr in cls.__dict__:
            if not attr.startswith('__') and not callable(getattr(cls, attr)):
                dic_attrs[attr] = getattr(cls, attr)
        return dic_attrs



if __name__ == "__main__" :
    d = tigerair_area_option_xpath.method_all_attrs()
    print(d)

