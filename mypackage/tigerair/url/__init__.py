__all__ = [
    "tigerair_url",
]

class tigerair_url:
    index = 'https://booking.tigerairtw.com/zh-TW/index'
    graphQL =  'https://api-book.tigerairtw.com/graphql'

    @classmethod
    def method_all_attrs(cls):
        dic_attrs = {}
        for attr in cls.__dict__:
            if not attr.startswith('__') and not callable(getattr(cls, attr)):
                dic_attrs[attr] = getattr(cls, attr)
        return dic_attrs