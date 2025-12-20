# world_data.py

WORLD_ROOMS = {

    "forest": {
        "name": "Forest",
        "description": (
            "Standing within a dense forest where trees crowd the pathway "
            "and branches weave themselves over and above you, disrupting any "
            "signs of light. The air feels heavy and still and is polluted with "
            "the same damp smell you smell after a rainstorm. Unaware of where to "
            "turn next, you feel the trees watching you and know you need to make a "
            "decision soon."
            "There are no clear pathways. You have to make a decison  "
        ),
        "look": (
            "Due to the thick vegetation, it remains hard to see what’s out there. "
            "Shadows move between the trees."
            "2 narrow openings reveal themselves to you. you can either choose to go East or South"
        ),
        "exits": {
            "south": "thicket",
            "east": "crashed_alien_pod"
        },
        "items": [],
        "alien": None,
        "effects": []
    },

    "thicket": {
        "name": "Thicket",
        "description": (
            "Past the bushes entangled and intertwined and overgrown. "
            "You come across a new area of the forest. Here, thick brambles"
            "and vines reach out to you in every direction. Grasping at your "
            "clothes, pricking you with every movement."
            "Even movement is challenging under the thick branches. But you realise"
            "you can use this to your advantage- the bushes present excellent cover to hide. "
            "the forest. Brambles and thorns tear at your skin."
        ),
        "look": (
            "While hidden, you can take the time to examine your surroundings."
            "Through the gaps in the branches you see there are two possible pathways.."
        ),
        "exits": {
            "north": "dense_forest",
            "west": "abandoned_campsite"
        },
        "items": [],
        "alien": None,
        "effects": [
            {
                "type": "damage",
                "amount": 25,
                "message": (
                    "The thorns cut into your skin as you progess forward. This will affect your help"
                )
            }
        ]
    },

    "abandoned_campsite": {
        "name": "Abandoned Campsite",
        "description": (
            "You finally reach an open stretch of land. "
            "Torn apart tents lay hapazardly on the grass. "
            "Old fire pits stand abandoned and dilapidated, "
            "surrounded by bags and supplies…almost as if this"
            "campsite had been suddenly and quickly abandoned. But why?"
        ),
        "look": (
            "The campsite looks recently deserted. Near an empty fire pit, "
            "you spot a medkit."
        ),
        "exits": {
            "east": "thicket",
            "north": "stream_bank",
            "south": "golden_nest"
        },
        "items": ["medkit"],
        "alien": "zorvath",
        "effects": []
    },

    "crashed_pod": {
        "name": "Crashed Alien Pod",
        "description" : (
            "Strobing lights pierce behind the bushes,"
            "nearly blinding you. Curious and full of wonder,"
            "you walk towards it in a trance-like state. A "
            "low hum fills the air."
        ),
        "look": (
           "In front of you- a crashed alien spaceship. This"
            "explains all of the occurrences. Suddenly you are "
            "filled with fear. Does this mean you will endure an "
            "attack? You need to act fast before its too late."
        ),
        "exists": {
            "south": "stream_bank",
            "west": "forest"
        },
       
        "items": ["plasma cell, cloaking shard"],
        "alien": "xexu",
        "effects": []

    },

    "golden_nest": {
        "name": "Golden Nest",
        "description": ("Stepping out into an open clearing,"
        " the trees beckon you into a circular open space bathed "
        "in golden sunlight. You feel happy."
        "Placed with near perfection, in the midst of this opening "
        "lies a glowing nest calling itself towards you. You want to "
        "respond to its beckon, but you know it could be a trap. It "
        "would be safe to survey your surroundings before making any decisions"),
        "look": (" "

        ),
        "items":["golden egg"],
        "alien": "Gronk",
        "effects": []
    },

    "stream_bank": {
        "name": "Stream Bank",
        "description": (
            "Whilst cautiously making your way through the forest,"
            "you soon come upon a shallow stream. Clear water flows "
            "calmly. The sound of the gentle stream briefly calms your nerves. "
            "This would be a good place to wash off any lingering alien scent "
            "and offer protection."
        ),
        "look": (
            "Beyond the stream, flickering lights probe through the trees. "
            "Something metallic lies ahead."
        ),
        "exits": {
            "north": "crashed_pod",
            "east": "abandoned_campsite"
        },
        "items": [],
        "alien": None,
        "effects": [
            {
                "type": "status",
                "status": "hidden",
                "duration": 3,
                "message": (
                    "Washing yourself masks your scent from alien creatures."
                )
            }
        ]
    }

}
