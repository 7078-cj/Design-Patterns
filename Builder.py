class NetworkService:
    def __init__(self):
        self.components = {}
        
    def add(self, key, value):
        self.components[key] = value
    
    def show(self):
        print('Network Service Components:')
        for key, value in self.components.items():
            print(f'{key}: {value}')
            
class NetworkServiceBuilder:
    def __init__(self):
        self._service = NetworkService()
        
    def add_target_url(self, url):
        self._service.add('Target URL', url)
        return self
    
    def add_auth(self, auth):
        self._service.add('Authentication', auth)
        return self
    
    def add_cache(self, cache):
        self._service.add('Cache', cache)
        return self
    
    def build(self):
        service = self._service #this will store the current state of the service
        self._service = NetworkService() #reset builder for next build
        return service #this will return the built service and 
                        #allow us to start building a new one 
                        # without affecting the previous one
    
if __name__ == '__main__':
    builder = NetworkServiceBuilder()
    service1 = (builder.add_target_url('https://api.example.com')
                        .add_auth('Bearer token')
                        .add_cache('Redis')
                        .build())
    
    service1.show()
    
    service2 = (builder.add_target_url('https://api.another.com')
                        .add_auth('Basic auth')
                        .build())
    
    service2.show()
    service1.show()