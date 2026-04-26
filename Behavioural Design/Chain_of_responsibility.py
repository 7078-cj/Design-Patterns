from __future__ import annotations
from abc import ABC, abstractmethod

class HandlerChain(ABC):
    def __init__(self, input_header):
        self.next_header = input_header
        
    @abstractmethod
    def add_header(self, input_header):
        pass
    
    def do_next(self, input_header):
        if self.next_header:
            return self.next_header.add_header(input_header)
        return input_header
    
class AuthenticationHeader(HandlerChain):
    def __init__(self, token, next_header=None):
        super().__init__(next_header)
        self.token = token
        
    def add_header(self, input_header):
        h = f"{input_header} | Authentication: {self.token}"
        return self.do_next(h)
    
class ContentTypeHeader(HandlerChain):
    def __init__(self, content_type, next_header=None):
        super().__init__(next_header)
        self.content_type = content_type
        
    def add_header(self, input_header):
        h = f"{input_header} | Content-Type: {self.content_type}"
        return self.do_next(h)
    
class BodyPayloadHeader(HandlerChain):
    def __init__(self, body, next_header=None):
        super().__init__(next_header)
        self.body = body
        
    def add_header(self, input_header):
        h = f"{input_header} | Body: {self.body}"
        return self.do_next(h)
    
if __name__ == "__main__":
    body = BodyPayloadHeader("Hello, World!")
    content_type = ContentTypeHeader("application/json")
    auth = AuthenticationHeader("mysecrettoken")
    
    auth.next_header = content_type
    content_type.next_header = body
    
    message_with_auth = auth.add_header("header with authentication")
    message_without_auth = content_type.add_header("header without authentication")
    
    print(message_with_auth)
    print()
    print(message_without_auth)
    