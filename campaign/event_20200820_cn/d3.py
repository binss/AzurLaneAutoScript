from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from .d1 import Config as ConfigBase

MAP = CampaignMap('D3')
MAP.shape = 'I7'
MAP.camera_data = ['D2', 'D5', 'F2', 'F5']
MAP.camera_data_spawn_point = ['D2', 'D5']
MAP.map_data = """
    MS -- -- ++ ++ -- -- -- --
    -- Me ME MS ++ -- ME -- --
    SP -- -- -- -- ME ++ ++ ++
    -- Me -- ++ -- -- -- -- MB
    SP -- ME __ -- ME ++ ++ ++
    Me -- ++ Me ME -- -- -- --
    -- Me ++ -- ME MS ME -- --
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    05 04 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2, 'siren': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1},
    {'battle': 6, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
    = MAP.flatten()


class Config(ConfigBase):
    MAP_SIREN_TEMPLATE = ['CL', 'CA', 'BB', 'CV']
    MOVABLE_ENEMY_TURN = (3,)
    MAP_HAS_SIREN = True
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = True


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.config.MAP_HAS_MOVABLE_ENEMY:
            self.fleet_2_push_forward()

        if self.clear_siren():
            return True
        if self.clear_enemy(scale=(3,), genre=['light', 'main', 'enemy', 'carrier']):
            return True

        return self.battle_default()

    def battle_5(self):
        if self.clear_enemy(scale=(1,)):
            return True
        if self.clear_enemy(scale=(2,), genre=['light', 'main', 'enemy', 'carrier']):
            return True
        if self.clear_enemy(genre=['light', 'main', 'enemy']):
            return True

        return self.battle_default()

    def battle_6(self):
        return self.fleet_boss.clear_boss()
