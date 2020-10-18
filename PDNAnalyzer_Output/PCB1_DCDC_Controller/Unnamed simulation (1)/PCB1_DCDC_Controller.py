designFile = "C:/Users/gmant/Desktop/PROJECTS/Celestial Projects/DCDC Buck Controller V2/DCDC Buck Controller V2/PDNAnalyzer_Output/PCB1_DCDC_Controller/odb.tgz"

powerNets = ["VIN", "SW", "VOUT"]

groundNets = ["PGND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "1") ],
"ground_pins": [ ("J1", "2") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J2", "2") ],
"ground_pins": [ ("J2", "1") ],
"current": 6,
"Rpin": 0.0166666666666667,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("IC3", "pdna_pin_D_1"), ("IC3", "pdna_pin_D_2"), ("IC3", "pdna_pin_D_3"), ("IC3", "pdna_pin_D_4") ],
"ground_pins": [ ("IC3", "pdna_pin_S_1"), ("IC3", "pdna_pin_S_2") ],
"resistance": 1E-09,
"Rpin": 13.3333333333333,
}
]


voltage_regulators = [
{
"id": "3",
"type": "linear",

"in": [ ("IC2", "pdna_pin_S_1"), ("IC2", "pdna_pin_S_2") ],
"out": [ ("IC2", "pdna_pin_D_1"), ("IC2", "pdna_pin_D_2"), ("IC2", "pdna_pin_D_3"), ("IC2", "pdna_pin_D_4") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0126666666666667,
}
,
{
"id": "4",
"type": "linear",

"in": [ ("L1", "1") ],
"out": [ ("L1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.00725,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'LAYER_1', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'LAYER_2', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
