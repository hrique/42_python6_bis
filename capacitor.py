#!/usr/bin/env python3
from ex3 import Creature, TransformCapability, TransformCreatureFactory


def show(label: str, creature: Creature) -> None:
    print(f" {label}:")
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    print("Testing Creature with transform capability")
    fabric = TransformCreatureFactory()
    show("base", fabric.create_base())
    show("evolved", fabric.create_evolved())


if __name__ == "__main__":
    main()
