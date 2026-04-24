from dataclasses import dataclass
class ComplexSystemStore:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}
        print(f'Reading data from {self.filepath}...')
        
    def store(self, key, value):
        self.cache[key] = value
        print(f'Stored {key}: {value} in cache')
        
    def read(self, key):
        value = self.cache.get(key, None)
        print(f'Read {key}: {value} from cache')
        return value
    
    def commit(self):
        print(f'Storing cached data to file {self.filepath}')
        
@dataclass
class User:
    login: str
    
    
#facade pattern provides a simplified interface to a complex system. In this example, the ComplexSystemStore is a complex system that handles data storage and retrieval, while the UserRepository is a facade that provides a simpler interface for managing user data without exposing the complexities of the underlying store.
class UserRepository:
    def __init__(self):
        self.system_preferences = ComplexSystemStore('user_data.txt')
        
    def add_user(self, user: User):
        self.system_preferences.store("USER_key", user.login)
        self.system_preferences.commit()
        
    def get_user(self, login: str):
        return self.system_preferences.read("USER_key")

if __name__ == '__main__':
    user_repo = UserRepository()
    user = User(login='john_doe')
    user_repo.add_user(user)
    retrieved_user = user_repo.get_user('john_doe')
    print(f'Retrieved user login: {retrieved_user}')
    