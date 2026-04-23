from abc import ABC, abstractmethod



class Country:
    pass

class USA(Country):
    pass

class Spain(Country):
    pass

class Japan(Country):
    pass

class CountryFactory(ABC):
    @abstractmethod
    def currency_factory(self, country) -> str:
        pass
    
class FiatCurrencyFactory(CountryFactory):
    def currency_factory(self, country) -> str:
        if isinstance(country, USA):
            return 'Dollar'
        elif isinstance(country, Spain):
            return 'Euro'
        elif isinstance(country, Japan):
            return 'Yen'
        else:
            raise ValueError('Invalid country')
        
class VirtualCurrencyFactory(CountryFactory):
    def currency_factory(self, country) -> str:
        if isinstance(country, USA):
            return 'Bitcoin'
        elif isinstance(country, Spain):
            return 'Ethereum'
        elif isinstance(country, Japan):
            return 'Dogecoin'
        else:
            raise ValueError('Invalid country')
        
        
if __name__ == '__main__':
    f1 = FiatCurrencyFactory()
    f2 = VirtualCurrencyFactory()
    
    print(f1.currency_factory(USA()))
    print(f1.currency_factory(Spain()))
    print(f1.currency_factory(Japan()))
    
    print(f2.currency_factory(USA()))
    print(f2.currency_factory(Spain()))
    print(f2.currency_factory(Japan()))
    
#sampe django use
# class NotificationFactory:
#     _notifiers = {
#         "email": EmailSender,
#         "sms": SMSSender,
#     }

#     def get_notifier(self, type):
#         notifier_class = self._notifiers.get(type)
#         if not notifier_class:
#             raise ValueError("Invalid type")
#         return notifier_class()