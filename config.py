# source: https://vancouver.housing.ubc.ca/residences-rooms/residences/
residences = {
    "BC": {
        "name": "Brock Commons",
        "units_by_size": { # key: units_by_size/unit, val: number of units
            1: 540+8+6,
            4: 112,
        },
        "beds": 1002,
    },
    "EX": {
        "name": "Exchange",
        "units_by_size": {
            1: 71+88+5+77,
            2: 19+15,
            4: 84,
        },
        "beds": 650,
    },
    "FH": {
        "name": "Fraser Hall",
        "units_by_size": {
            6: 22,
        },
        "beds": 132,
    },
    "IH": {
        "name": "Iona House",
        "units_by_size": {
            1: 13+4,
            2: 3,
        },
        "beds": 23,
    },
    "KW": {
        "name": "Saltwater",
        "units_by_size": {
            1: 505+20+7,
            4: 54,
        },
        "beds": 744,
    },
    "MD": {
        "name": "Marine Drive",
        "units_by_size": {
            1: 274,
            2: 10,
            3: 29,
            4: 307,
        },
        "beds": 1603,
    },
    "PC": {
        "name": "Ponderosa Commons",
        "units_by_size": {
            1: 615+11,
            2: 113,
            4: 76,
        },
        "beds": 1156,
    },
    "TB": {
        "name": "Thunderbird",
        "units_by_size": {
            1: 167+153,
            2: 9,
            4: 74,
        },
        "beds": 634,
    },
}

def sum_beds(units_dict: dict) -> int:
    total_beds = 0
    for num_beds, num_units in units_dict.items():
        total_beds += num_units * num_beds
    return total_beds

if __name__ == '__main__':
    # validate bed count -- should be redundant
    for residence in residences.values():
        print(f"{residence['name']: <18} expected: {residence['beds']: <6} "
              f"counted: {sum_beds(residence['units_by_size']): <6}"
              f"difference: {abs(sum_beds(residence['units_by_size']) - residence['beds'])}")
