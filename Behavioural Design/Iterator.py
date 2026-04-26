
class AlphabeticalOrderIterator:
    def __init__(self, words, reverse = False):
        self.collection = sorted(words)
        self.reverse = reverse
        self.position = len(self.collection) - 1 if reverse else 0
        
    def next(self):
        value = self.collection[self.position]
        self.position += -1 if self.reverse else 1
        return value
    
    def has_next(self):
        if self.reverse and self.position >= 0:
            return True
        elif not self.reverse and self.position < len(self.collection):
            return True
        else:
            return False
        
class WordsCollection:
    def __init__(self, collection):
        self.collection = collection
        
    def get_iterator(self):
        return AlphabeticalOrderIterator(self.collection)
    
    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self.collection, reverse=True)
    
if __name__ == "__main__":
    collection = WordsCollection(["apple", "banana", "cherry", "date", "fig"])
    iterator = collection.get_iterator()
    reverse_iterator = collection.get_reverse_iterator()
    
    while iterator.has_next():
        print(iterator.next())
    
    print()
    
    while reverse_iterator.has_next():
        print(reverse_iterator.next())
        
    