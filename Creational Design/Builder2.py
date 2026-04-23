
class NetworkService:
    def __init__(self, url='', auth='', cache=0):
        self.components={}
        
        if url:
            self.components['Target URL'] = url
        if auth:
            self.components['Authentication'] = auth
        if cache:
            self.components['Cache'] = cache
            
    def show(self):
        print('Network Service Components:')
        for key, value in self.components.items():
            print(f'{key}: {value}')
            
if __name__ == '__main__':
    service1 = NetworkService(url='https://api.example.com', auth='Bearer token', cache=100)
    service1.show()
    service2 = NetworkService(url='https://api.another.com', auth='Basic auth')
    service2.show()