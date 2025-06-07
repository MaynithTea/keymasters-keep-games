from __future__ import annotations

import functools
from typing import List
from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class Splatoon3ArchipelagoOptions:
    splatoon_3_weapons: Splatoon3Weapons
    splatoon_3_modes: Splatoon3Modes


class Splatoon3Game(Game):
    name = "Splatoon 3"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = Splatoon3ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = list()

        if "Regular Battle" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Win a Regular Battle using the WEAPON",
                    data={
                        "WEAPON": (self.weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=70,
                ),
                GameObjectiveTemplate(
                    label="Win a Regular Battle using the WEAPON and the abilities HEAD, SHIRT, and SHOE",
                    data={
                        "WEAPON": (self.weapons, 1),
                        "HEAD": (self.headgear, 1),
                        "SHIRT": (self.clothes, 1),
                        "SHOE": (self.shoes, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=35,
                ),
            ])

        if "Anarchy Battle" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Win a ANARCHY match using the WEAPON",
                    data={
                        "ANARCHY": (self.anarchy_modes, 1),
                        "WEAPON": (self.weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=500,
                ),
                GameObjectiveTemplate(
                    label="Win a ANARCHY match using the WEAPON and the abilities HEAD, SHIRT, and SHOE",
                    data={
                        "ANARCHY": (self.anarchy_modes, 1),
                        "WEAPON": (self.weapons, 1),
                        "HEAD": (self.headgear, 1),
                        "SHIRT": (self.clothes, 1),
                        "SHOE": (self.shoes, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=250,
                ),
            ])

        if "Salmon Run" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Win a round of Salmon Run with at least EGG golden eggs",
                    data={
                        "EGG": (self.egg_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=15,
                ),
            ])

        if "Alterna" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Complete mission: CRATER at The Crater",
                    data={
                        "CRATER": (self.crater_missions, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE1 at Site 1",
                    data={
                        "SITE1": (self.alterna_site1, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE2 at Site 2",
                    data={
                        "SITE2": (self.alterna_site2, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE3 at Site 3",
                    data={
                        "SITE3": (self.alterna_site3, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE4 at Site 4",
                    data={
                        "SITE4": (self.alterna_site4, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE5 at Site 5",
                    data={
                        "SITE5": (self.alterna_site5, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: SITE6 at Site 6",
                    data={
                        "SITE6": (self.alterna_site6, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: Rocket Battle",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete mission: After Alterna",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=15,
                ),
            ])

        if "Side Order" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Clear Floor 30 using PALETTE Palette",
                    data={
                        "PALETTE": (self.palettes, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Clear Floor 30 using PALETTE Palette and no vending machine visits",
                    data={
                        "PALETTE": (self.palettes, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=10,
                ),
                GameObjectiveTemplate(
                    label="Clear Floor 30 using PALETTE Palette with no more than MARINA Marina hacks",
                    data={
                        "PALETTE": (self.palettes, 1),
                        "MARINA": (self.egg_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=10,
                ),
                GameObjectiveTemplate(
                    label="Clear Floor 30 using PALETTE Palette with no more than MARINA Marina hacks and no vending machine visits",
                    data={
                        "PALETTE": (self.palettes, 1),
                        "MARINA": (self.egg_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=5,
                ),
            ])

        if "Tableturf Battle" in self.modes():
            templates.extend([
                GameObjectiveTemplate(
                    label="Win a Tableturf Battle against OPPONENT at Lv. LEVEL",
                    data={
                        "OPPONENT": (self.tableturf_opponents, 1),
                        "LEVEL": (self.tableturf_level, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=15,
                ),
            ])

        return templates

    def weapons(self) -> List[str]:
        return sorted(self.archipelago_options.splatoon_3_weapons.value)

    def modes(self) -> List[str]:
        return sorted(self.archipelago_options.splatoon_3_modes.value)

    @staticmethod
    def anarchy_modes() -> List[str]:
        return [
            "Splat Zones",
            "Tower Control",
            "Rainmaker",
            "Clam Blitz",
        ]

    @staticmethod
    def egg_range() -> range:
        return range(12, 70)

    @staticmethod
    def crater_missions() -> List[str]:
        return [
            "Octarians in the Crater? YIKES!",
            "Sink into the Ink and SWIM!",
            "Boxes Locked! Keys, Please!",
            "What Are They? Can We Stop Them?!",
            "Octobot King L3.Gs",
        ]

    @staticmethod
    def alterna_site1() -> List[str]:
        return [
            "Get to Know Alterna, Your Only Choice",
            "Octopods at Rest Tend to FLIP OUT!",
            "Splat You on the Flip Side",
            "Doors, Doors, Doors! And More! (Doors)",
            "Relic Restoration",
            "Zip, Splat, and Jump",
            "Become One with Your Smallfry",
            "What Caused the Big Bang? YOU!",
            "The String's the Thing",
            "Deadly Dance Hall—Jump, Jump!",
        ]

    @staticmethod
    def alterna_site2() -> List[str]:
        return [
            "Twirling, Swirling, Whirling",
            "Absorbency and You",
            "Soak It to Me!",
            "Splitting Crosshairs",
            "Tread Heavily",
            "Getting Lost in Three Easy Steps",
            "The Ink-Conservation Project",
            "Switching Things Up",
            "The Future Stares Back",
        ]

    @staticmethod
    def alterna_site3() -> List[str]:
        return [
            "Climbing the Corporate Splatter",
            "They Said We'd Have Flying Cars, and We Do! Kinda!",
            "Ink Wheels—Experience Tomorrow's Technology Today!",
            "Try Curling! Alterna's 11th Most Popular Athleisure Activity!",
            "Conveyor-Belt Tightening",
            "Time Trial and Errors",
            "Rail Pass",
        ]

    @staticmethod
    def alterna_site4() -> List[str]:
        return [
            "Propellered to Greatness",
            "Octohoppers Don't Have a Sense of Humor (and They Hate Puns)!",
            "Let's Put a Pin in That",
            "Splash the Block Party",
            "Amusing a Bemused Muse",
            "Those Aren't Birds",
            "Charge Now, Splat Later",
            "Easy Ride, Tricky Targets",
            "Flying Worst Class",
            "Ink Fast, Hotshot",
            "Stamp 'Em Out",
            "The Path to Perfect Penmanship",
            "The Pursuit of the Precious",
        ]

    @staticmethod
    def alterna_site5() -> List[str]:
        return [
            "Trouble Round Every Corner",
            "The Upside to Enemy Backsides",
            "Uh-Oh! Too Many Snipers!",
            "Barriers! They've Got You Covered",
            "A Compulsive Collector's Paradise",
            "Zipping over the Neighborhood",
            "One-Way Ride through Target Town",
            "Making Waves with Splashdowns",
            "Low Viz, High Risk",
            "Shooter on Rails",
            "Simply Zipcastic!",
            "You'll Go Far If You Shoot Far",
            "Learn to Reflect, and This One Is in the Bank",
        ]

    @staticmethod
    def alterna_site6() -> List[str]:
        return [
            "Bet You Mist Us!",
            "Octarian Heights",
            "Torture Tour",
            "Conserve Ink—Splat Sustainably",
            "The Enemy Ink Is Lava!",
            "Keep It Rolling",
            "That Sinking Feeling",
            "Breathe In, Breathe Out",
            "Dive and Dash",
            "Mission: Fly-Fishin'",
            "Don't Tease with the Keys",
            "Enter the Stamp Gauntlet",
            "The Obscurest Chiaroscurist",
        ]

    @staticmethod
    def palettes() -> List[str]:
        return [
            "Pearl's",
            "Marina's",
            "Agent 4's",
            "Callie's",
            "Marie's",
            "Shiver's",
            "Frye's",
            "Big Man's",
            "Murch's",
            "Sheldon's",
            "DJ Octavio's",
            "Eight's",
        ]

    @staticmethod
    def tableturf_opponents() -> List[str]:
        return [
            "Baby Jelly",
            "Cool Jelly",
            "Aggro Jelly",
            "Sheldon",
            "Gnarly Eddy",
            "Jel La Fleur",
            "Mr. Coco",
            "Harmony",
            "Judd",
            "Li'l Judd",
            "Murch",
            "Shiver",
            "Frye",
            "Shelly",
            "Annie",
            "Jelonzo",
            "Fred Crumbs",
            "Spyke",
            "Flow",
            "Jelfonzo",
            "Bisk",
            "Pearl",
            "Marina",
            "Acht",
        ]

    @staticmethod
    def tableturf_level() -> range:
        return range(1, 3)

    @staticmethod
    def universal_abilities() -> List[str]:
        return [
            "Ink Saver (Main)",
            "Ink Saver (Sub)",
            "Ink Recovery Up",
            "Run Speed Up",
            "Swim Speed Up",
            "Special Charge Up",
            "Special Saver",
            "Special Power Up",
            "Quick Respawn",
            "Quick Super Jump",
            "Sub Power Up",
            "Ink Resistance Up",
            "Sub Resistance Up",
            "Intensify Action",
        ]

    @staticmethod
    def headgear_abilities() -> List[str]:
        return [
            "Opening Gambit",
            "Last-Ditch Effort",
            "Tenacity",
            "Comeback",
        ]

    @staticmethod
    def clothes_abilities() -> List[str]:
        return [
            "Ninja Squid",
            "Haunt",
            "Thermal Ink",
            "Respawn Punisher",
        ]

    @staticmethod
    def shoes_abilities() -> List[str]:
        return [
            "Stealth Jump",
            "Object Shredder",
            "Drop Roller",
        ]

    def headgear(self) -> List[str]:
        headgear: List[str] = self.universal_abilities() + self.headgear_abilities()

        return sorted(headgear)

    def clothes(self) -> List[str]:
        clothes: List[str] = self.universal_abilities() + self.clothes_abilities()

        return sorted(clothes)

    def shoes(self) -> List[str]:
        shoes: List[str] = self.universal_abilities() + self.shoes_abilities()

        return sorted(shoes)

# Archipelago Options
class Splatoon3Weapons(OptionSet):
    """
    Indicates which Splatoon 3 Weapons the player has access to.
    """

    display_name = "Splatoon 3 Weapons Bought"
    valid_keys = [
        "Sploosh-o-matic",
        "Neo Sploosh-o-matic",
        "Splattershot Jr.",
        "Custom Splattershot Jr.",
        "Splash-o-matic",
        "Neo Splash-o-matic",
        "Aerospray MG",
        "Aerospray RG",
        "Splattershot",
        "Tentatek Splattershot",
        "Hero Shot Replica",
        "Octo Shot Replica",
        "Order Shot Replica",
        ".52 Gal",
        ".52 Gal Deco",
        "N-ZAP '85",
        "N-ZAP '89",
        "Splattershot Pro",
        "Forge Splattershot Pro",
        ".96 Gal",
        ".96 Gal Deco",
        "Jet Squelcher",
        "Custom Jet Squelcher",
        "Splattershot Nova",
        "Annaki Splattershot Nova",
        "L-3 Nozzlenose",
        "L-3 Nozzlenose D",
        "H-3 Nozzlenose",
        "H-3 Nozzlenose D",
        "Squeezer",
        "Foil Squeezer",
        "Carbon Roller",
        "Carbon Roller Deco",
        "Splat Roller",
        "Krak-On Splat Roller",
        "Order Roller Replica",
        "Dynamo Roller",
        "Gold Dynamo Roller",
        "Flingza Roller",
        "Foil Flingza Roller",
        "Big Swig Roller",
        "Big Swig Roller Express",
        "Classic Squiffer",
        "New Squiffer",
        "Splat Charger",
        "Z+F Splat Charger",
        "Order Charger Replica",
        "Splatterscope",
        "Z+F Splatterscope",
        "E-liter 4K",
        "Custom E-liter 4K",
        "E-liter 4K Scope",
        "Custom E-liter 4K Scope",
        "Bamboozler 14 Mk I",
        "Bamboozler 14 Mk II",
        "Goo Tuber",
        "Custom Goo Tuber",
        "Snipewriter 5H",
        "Snipewriter 5B",
        "Slosher",
        "Slosher Deco",
        "Order Slosher Replica",
        "Tri-Slosher",
        "Tri-Slosher Nouveau",
        "Sloshing Machine",
        "Sloshing Machine Neo",
        "Bloblobber",
        "Bloblobber Deco",
        "Explosher",
        "Custom Explosher",
        "Dread Wringer",
        "Dread Wringer D",
        "Mini Splatling",
        "Zink Mini Splatling",
        "Heavy Splatling",
        "Heavy Splatling Deco",
        "Order Splatling Replica",
        "Hydra Splatling",
        "Custom Hydra Splatling",
        "Ballpoint Splatling",
        "Ballpoint Splatling Nouveau",
        "Nautilus 47",
        "Nautilus 79",
        "Heavy Edit Splatling",
        "Heavy Edit Splatling Nouveau",
        "Dapple Dualies",
        "Dapple Dualies Nouveau",
        "Splat Dualies",
        "Enperry Splat Dualies",
        "Order Dualies Replica",
        "Glooga Dualies",
        "Glooga Dualies Deco",
        "Dualie Squelchers",
        "Custom Dualie Squelchers",
        "Dark Tetra Dualies",
        "Light Tetra Dualies",
        "Douser Dualies FF",
        "Custom Douser Dualies FF",
        "Splat Brella",
        "Sorella Brella",
        "Order Brella Replica",
        "Tenta Brella",
        "Tenta Sorella Brella",
        "Undercover Brella",
        "Undercover Sorella Brella",
        "Recycled Brella 24 Mk I",
        "Recycled Brella 24 Mk II",
        "Luna Blaster",
        "Luna Blaster Neo",
        "Order Blaster Replica",
        "Blaster",
        "Custom Blaster",
        "Range Blaster",
        "Custom Range Blaster",
        "Clash Blaster",
        "Clash Blaster Neo",
        "Rapid Blaster",
        "Rapid Blaster Deco",
        "Rapid Blaster Pro",
        "Rapid Blaster Pro Deco",
        "S-BLAST '92",
        "S-BLAST '91",
        "Inkbrush",
        "Inkbrush Nouveau",
        "Octobrush",
        "Octobrush Nouveau",
        "Orderbrush Replica",
        "Painbrush",
        "Painbrush Nouveau",
        "Tri-Stringer",
        "Inkline Tri-Stringer",
        "Order Stringer Replica",
        "REEF-LUX 450",
        "REEF-LUX 450 Deco",
        "Wellstring V",
        "Custom Wellstring V",
        "Splatana Stamper",
        "Splatana Stamper Nouveau",
        "Order Splatana Replica",
        "Splatana Wiper",
        "Splatana Wiper Deco",
        "Mint Decavitator",
        "Charcoal Decavitator",
    ]

    default = valid_keys

class Splatoon3Modes(OptionSet):
    """
    Indicates which Splatoon 3 Modes should be used when generating objectives.
    """

    display_name = "Splatoon 3 Modes"
    valid_keys = [
        "Regular Battle",
        "Anarchy Battle",
        "Salmon Run",
        "Alterna",
        "Side Order",
        "Tableturf Battle",
    ]

    default = valid_keys