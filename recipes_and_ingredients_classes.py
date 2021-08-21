""" Recipes and Ingredients Classes

This file contains the important classes that represent recipes, ingredients, instructions etc.
"""
from __future__ import annotations
from typing import Optional, Dict


class Ingredient:
    """A class representing ingredients in a recipe.

    Instance Attributes:
        - name: The name of the ingredient
        - is_mandatory: Whether it is a mandatory ingredient or not.
        - amount: The amount of this ingredient required
        - alternatives: Alternative ingredients that can be used instead of this one.
                        Maps ingredient names to Ingredient objects

    Representation Invariants:
        - all(name == alternatives[name].name for name in alternatives)
    """
    name: str
    is_mandatory: bool
    amount: str
    alternatives: Dict[str, Ingredient]

    def __init__(self, name: str, amount: str, alternatives: Optional[Dict[str, Ingredient]],
                 is_mandatory: bool = True) -> None:
        self.name = name
        self.amount = amount

        self.is_mandatory = is_mandatory

        if alternatives is not None:
            self.alternatives = alternatives
        else:
            self.alternatives = {}

    def __str__(self) -> str:
        return self.amount + ' ' + self.name + '. ' + str(len(self.alternatives)) + \
               ' alternatives.'


class Instruction:
    """A class representing an instruction of a recipe.

    Instance Attributes:
        - ingredients: A mapping of ingredients' names to the objects for the ingredients
                    required for this instruction.
        - instruction: The actual instructions required for the current step.
        - duration: The length of this step in minutes.
    """
    ingredients: Dict[str, Ingredient]
    instruction: str
    duration: float

    def __init__(self, ingredients: Dict[str, Ingredient], instruction: str,
                 duration: float) -> None:

        self.ingredients = ingredients
        self.instruction = instruction
        self.duration = duration

    def __str__(self) -> str:
        return self.instruction


class Recipe:
    """A class representing a recipe.

    Instance Attributes:
        - instructions: A list of instructions for the recipe
        - ingredients: A list of ingredients needed for the recipe
        - total_time: The total time required for the recipe in minutes.
    """
    instructions: list[Instruction]
    ingredients: list[Ingredient]
    total_time: float

    def __init__(self, instructions: list[Instruction], ingredients: list[Ingredient],
                 total_time: float) -> None:
        self.ingredients = ingredients
        self.instructions = instructions
        self.total_time = total_time

    # def __str__(self) -> str:
    #     pass
