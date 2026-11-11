from abc import ABC, abstractmethod

from ex3 import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    name: str = "Battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        # TODO: serve para qualquer criatura
        return False

    def act(self, creature: Creature) -> None:
        # TODO: imprimir o attack da criatura
        pass


class AggressiveStrategy(BattleStrategy):
    name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        # TODO: só serve para quem tem TransformCapability (isinstance)
        return False

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            # TODO: raise InvalidStrategyError com a mensagem
            #   Invalid Creature '<nome>' for this aggressive strategy
            return
        # TODO: imprimir transform, attack, revert
