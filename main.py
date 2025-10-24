import random as rnd

RUNES = [
    {
        "name": "Precision",
        "major_runes": [
            1, #Press the Attack
            2, #Lethal Tempo
            3, #Fleet Footwork
            4  #Conqueror
        ],
        "minor_runes": [
            [
                78, #Absorb Life
                17, #Triumph
                18  #Presence of Mind
            ],
            [
                19, #Legend: Alacrity
                79, #Legend: Haste
                21  #Legend: Bloodline
            ],
            [
                22, #Coup de Grace
                23, #Cut Down
                24  #Last Stand
            ]
        ]
    },
    {
        "name": "Domination",
        "major_runes": [
            4, #Electrocute
            6, #Dark Harvest
            71  #Hail of Blades
        ],
        "minor_runes": [
            [
                28, #Cheap Shot
                29, #Taste of Blood
                30  #Sudden Impact
            ],
            [
                83, #Sixth Sense
                84, #Grisly Mementos
                85  #Deep Ward
            ],
            [
                76, #Treasure Hunter
                33, #Relentless Hunter
                72  #Ultimate Hunter
            ]
        ]
    },
    {
        "name": "Sorcery",
        "major_runes": [
            7, #Summon Aery
            8, #Arcane Comet
            9  #Phase Rush
        ],
        "minor_runes": [
            [
                82, #Axiom Arcanist
                35, #Manaflow Band
                70  #Nimbus Cloak
            ],
            [
                37, #Transcendence
                38, #Celerity
                39  #Absolute Focus
            ],
            [
                40, #Scorch
                41, #Waterwalking
                42  #Gathering Storm
            ]
        ]
    },
    {
        "name": "Resolve",
        "major_runes": [
            10, #Grasp of the Undying
            12, #Aftershock
            11  #Guardian
        ],
        "minor_runes": [
            [
                44, #Demolish
                45, #Font of Life
                73  #Shield Bash    
            ],
            [
                48, #Conditioning
                51, #Second Wind
                66  #Bone Plating
            ],
            [
                49, #Overgrowth
                50, #Revitalize
                43  #Unflinching
            ]
        ]
    },
    {
        "name": "Inspiration",
        "major_runes": [
            13, #Glacial Augment
            14, #Unsealed Spellbook
            75  #First Strike
        ],
        "minor_runes": [
            [
                52, #Hextech Flashtraption
                55, #Magical Footwear
                80  #Cash Back
            ],
            [
                77, #Triple Tonic
                67, #Time Warp Tonic
                53  #Biscuit Delivery
            ],
            [
                58, #Cosmic Insight
                59, #Approach Velocity
                81  #Jack of all Trades
            ]
        ]
    }
]

SHARDS = [
    [
        1,
        2,
        3
    ],
    [
        1,
        7,
        8
    ],
    [
        6,
        5,
        8
    ]
]




PRIMARY_PATH = RUNES.pop(rnd.randint(0, 4))
SECONDARY_PATH = RUNES.pop(rnd.randint(0, 3))

MAJOR_RUNE = PRIMARY_PATH.get("major_runes")[rnd.randint(0, len(PRIMARY_PATH.get("major_runes")) - 1)]

PRIMARY_MINOR_RUNES = [runes[rnd.randint(0, 2)] for runes in PRIMARY_PATH.get("minor_runes")]
PMR = PRIMARY_MINOR_RUNES #For readability

SECONDARY_MINOR_RUNES = [runes[rnd.randint(0, 2)] for runes in [SECONDARY_PATH.get("minor_runes").pop(rnd.randint(0, len(SECONDARY_PATH.get("minor_runes")) - 1)) for i in range(2)]]
SMR = SECONDARY_MINOR_RUNES #For readability

SELECTED_SHARDS = [shards[rnd.randint(0, 2)] for shards in SHARDS]
S = SELECTED_SHARDS

print(f'https://www.mobafire.com/league-of-legends/rune-page-planner#&rune={PRIMARY_PATH.get("name")}:{MAJOR_RUNE}:{PMR[0]}:{PMR[1]}:{PMR[2]}::{SECONDARY_PATH.get("name")}:{SMR[0]}:{SMR[1]}:::Shards:{S[0]}:{S[1]}:{S[2]}')