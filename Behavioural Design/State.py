from __future__ import annotations
import random
from abc import ABC, abstractmethod

class Game:
    def __init__(self):
        self.state = WelcomeScreenState(self)
        
    def change_state(self, state):
        self.state = state
        
class State(ABC):
    def __init__(self, game):
        self.game = game
        print(f' Currently in {self}')
        
    @abstractmethod
    def on_welcome_screen(self):
        pass
    
    @abstractmethod
    def on_playing(self):
        pass
    @abstractmethod
    def on_break(self):
        pass
    
    @abstractmethod
    def on_end_game(self):
        pass
    
class WelcomeScreenState(State):
    def on_welcome_screen(self):
        print("Currently on Welcome Screen")
    
    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("Not allowed from W to B")
    
    def on_end_game(self):
        print("Not allowed from W to EG")
    
class PlayingState(State):
    def on_welcome_screen(self):
        print("Not allowed from P to W")
    
    def on_playing(self):
        print("currently playing")

    def on_break(self):
        self.game.change_state(BreakState(self.game))
    
    def on_end_game(self):
        self.game.change_state(EndGameState(self.game))
    
class BreakState(State):
    def on_welcome_screen(self):
        print("Not allowed from B to W")
    
    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("currently on break")
    
    def on_end_game(self):
        print("Not allowed from B to EG")
    
class EndGameState(State):
    def on_welcome_screen(self):
        self.game.change_state(WelcomeScreenState(self.game))
    
    def on_playing(self):
        print("Not allowed from EG to P")

    def on_break(self):
        print("Not allowed from EG to B")
    
    def on_end_game(self):
        print("currently on end game")
        
if __name__ == '__main__':
    game = Game()
    
    for i in range(20):
        state = random .randrange(4)
        if state == 0:
            print("Moving to welcome")
            game.state.on_welcome_screen()
        elif state == 1:
            print("Moving to Playing")
            game.state.on_playing()
        elif state == 2:
            print("Moving to Break")
            game.state.on_break()
        elif state == 3:
            print("Moving to End Game")
            game.state.on_end_game()