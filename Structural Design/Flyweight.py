import random
from abc import ABC, abstractmethod


class Sprite(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def move(self, x, y):
        pass



class FighterRank:
    private = 0
    sergeant = 1
    major = 2



class Fighter(Sprite):
    def __init__(self, rank):
        self.rank = rank  # intrinsic (shared)

    def draw(self, x, y):
        print(f"Drawing {self.get_rank_name()} at ({x}, {y})")

    def move(self, x, y):
        print(f"Moving {self.get_rank_name()} to ({x}, {y})")

    def get_rank_name(self):
        if self.rank == FighterRank.major:
            return "Major"
        elif self.rank == FighterRank.sergeant:
            return "Sergeant"
        return "Private"


class FighterFactory:
    def __init__(self):
        self._fighters = {}  # cache

    def get_fighter(self, rank):
        if rank not in self._fighters:
            print(f"[Factory] Creating new fighter for rank {rank}")
            self._fighters[rank] = Fighter(rank)
        return self._fighters[rank]

    def total_created(self):
        return len(self._fighters)


class Soldier:
    def __init__(self, fighter, x, y):
        self.fighter = fighter  # shared object
        self.x = x              # unique
        self.y = y              # unique

    def draw(self):
        self.fighter.draw(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.fighter.move(x, y)


class Army:
    def __init__(self):
        self.soldiers = []
        self.factory = FighterFactory()

    def spawn_fighter(self, rank):
        fighter = self.factory.get_fighter(rank)

        # each soldier has its own position (extrinsic)
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        soldier = Soldier(fighter, x, y)
        self.soldiers.append(soldier)

    def draw_army(self):
        for soldier in self.soldiers:
            soldier.draw()

    def summary(self):
        print("\n--- Army Summary ---")
        print(f"Total soldiers: {len(self.soldiers)}")
        print(f"Unique fighter objects created: {self.factory.total_created()}")



if __name__ == "__main__":
    army_size = 1000
    army = Army()

    for _ in range(army_size):
        rank = random.randrange(3)
        army.spawn_fighter(rank)

    army.summary()