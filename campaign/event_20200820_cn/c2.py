from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from .c1 import Config as ConfigBase

MAP = CampaignMap('C2')
MAP.shape = 'G7'
MAP.camera_data = ['D3', 'D5']
MAP.camera_data_spawn_point = ['D5']
MAP.map_data = """
    -- -- -- -- -- -- MB
    ME -- -- ++ ++ ++ --
    -- ME __ -- ME Me --
    ME -- -- ME -- -- --
    ++ ME -- -- -- Me --
    -- -- -- MS -- ++ --
    SP SP -- ME -- ++ MB
"""
MAP.weight_data = """
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
    10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    # {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 0, 'enemy': 2, 'siren': 1},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, \
A2, B2, C2, D2, E2, F2, G2, \
A3, B3, C3, D3, E3, F3, G3, \
A4, B4, C4, D4, E4, F4, G4, \
A5, B5, C5, D5, E5, F5, G5, \
A6, B6, C6, D6, E6, F6, G6, \
A7, B7, C7, D7, E7, F7, G7, \
    = MAP.flatten()


class Config(ConfigBase):
    MAP_SIREN_TEMPLATE = ['Sheffield', 'Dorsetshire', 'Renown']
    MOVABLE_ENEMY_TURN = (3,)
    MAP_HAS_SIREN = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True

        return self.battle_default()

    def battle_4(self):
        return self.fleet_boss.clear_boss()
