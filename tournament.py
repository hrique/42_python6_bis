#!/usr/bin/env python3
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 InvalidStrategyError)

Opponent = tuple[CreatureFactory, BattleStrategy]


def show_opponents(title: str, opponents: list[Opponent]) -> None:
    print(title)
    names = [f"({f.create_base().name}+{s.name})" for f, s in opponents]
    print(" [ " + ", ".join(names) + " ]")


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [(f.create_base(), s) for f, s in opponents]
    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                c1, s1 = fighters[i]
                c2, s2 = fighters[j]
                # TODO: "\n* Battle *", describe de c1, " vs.",
                #       describe de c2, " now fight!",
                #       e a estratégia de cada um agindo (act)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    t0: list[Opponent] = [(flame, normal), (transform, aggressive)]
    show_opponents("Tournament 0 (basic)", t0)
    battle(t0)
    print()
    # TODO: "Tournament 1 (error)" com
    #       [(transform, aggressive), (flame, aggressive)]


if __name__ == "__main__":
    main()
