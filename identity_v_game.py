from __future__ import annotations

import functools
from typing import List
from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class IdentityVArchipelagoOptions:
    identity_v_hunters: IdentityVHunters
    identity_v_survivors: IdentityVSurvivors


class IdentityVGame(Game):
    name = "Identity V"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = IdentityVArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="As HUNTER send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Detention and Confined Space, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Detention and Insolence, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Detention and Trump Card, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Insolence and Confined Space, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Insolence and Trump Card, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using the final triats Trump Card and Confined Space, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using ONLY the final triat Insolence, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using ONLY the final triat Confined Space, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using ONLY the final triat Trump Card, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As HUNTER using ONLY the final triat Detention, send COUNT survivors to the manor",
                data={
                    "HUNTER": (self.hunters, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR achieve a result of COUNT survivors escaping",
                data={
                    "SURVIVOR": (self.survivors, 1),
                    "COUNT": (self.medium_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Knee Jerk Reflex and Borrowed Time, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Flywheel Effect and Borrowed Time, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Tide Turner and Borrowed Time, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Knee Jerk Reflex and Flywheel Effect, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Knee Jerk Reflex and Tide Turner, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using the final triats Flywheel Effect and Tide Turner, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using ONLY the final triat Knee Jerk Reflex, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using ONLY the final triat Flywheel Effect, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using ONLY the final triat Borrowed Time, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="As SURVIVOR using ONLY the final triat Tide Turner, escape",
                data={
                    "SURVIVOR": (self.survivors, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    def hunters(self) -> List[str]:
        return sorted(self.archipelago_options.identity_v_hunters.value)

    def survivors(self) -> List[str]:
        return sorted(self.archipelago_options.identity_v_survivors.value)

    @staticmethod
    def medium_range() -> range:
        return range(1, 4)


# Archipelago Options
class IdentityVHunters(OptionSet):
    """
    Indicates which Identity V Hunters the player has access to.
    """

    display_name = "Identity V Hunters Unlocked"
    valid_keys = [
        "Hell Ember",
        "Smiley Face",
        "Gamekeeper",
        "The Ripper",
        "Soul Weaver",
        "Geisha",
        "Wu Chang",
        "Photographer",
        "Mad Eyes",
        "The Feaster",
        "Dream Witch",
        "Axe Boy",
        "Evil Reptilian",
        "Bloody Queen",
        "Bonbon",
        "Disciple",
        "Violinist",
        "Sculptor",
        "Undead",
        "The Breaking Wheel",
        "Naiad",
        "Wax Artist",
        "Nightmare",
        "Clerk",
        "Hermit",
        "Night Watch",
        "Opera Singer",
        "Fool's Gold",
        "The Shadow",
        "Goatman",
        "Hullabaloo",
        "Peddler",
    ]

    default = valid_keys


class IdentityVSurvivors(OptionSet):
    """
    Indicates which Identity V Survivors the player has access to.
    """

    display_name = "Identity V Survivors Unlocked"
    valid_keys = [
        "Doctor",
        "Lawyer",
        "Thief",
        "Gardener",
        "Magician",
        "Explorer",
        "Mercenary",
        "Coordinator",
        "Priestess",
        "Mechanic",
        "Forward",
        "The Mind's Eye",
        "Perfumer",
        "Cowboy",
        "Female Dancer",
        "Seer",
        "Embalmer",
        "Prospector",
        "Enchantress",
        "Wildling",
        "Acrobat",
        "First Officer",
        "Barmaid",
        "Postman",
        "Grave Keeper",
        "Prisoner",
        "Entomologist",
        "Painter",
        "Batter",
        "Toy Merchant",
        "Patient",
        "Psychologist",
        "Novelist",
        "Little Girl",
        "Weeping Clown",
        "Professor",
        "Antiquarian",
        "Composer",
        "Journalist",
        "Aeroplanist",
        "Cheerleader",
        "Puppeteer",
        "Fire Investigator",
        "Faro Lady",
        "Knight",
        "Meteorologist",
        "Archer",
        "Escapologist",
        "Lucky Guy",
    ]

    default = valid_keys
