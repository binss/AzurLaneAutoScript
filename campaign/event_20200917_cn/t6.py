from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from .campaign_base import CampaignBase
from .t1 import Config as ConfigBase

MAP = CampaignMap('T6')
MAP.shape = 'K10'
# MAP.camera_data = ['D2', 'D6', 'D8', 'H2', 'H6', 'H8']
MAP.camera_data = ['D2', 'D6', 'G2', 'G6']
MAP.camera_data_spawn_point = ['D6', 'G6']
MAP.map_data = """
    -- -- -- ME -- Me -- ME -- -- --
    -- ++ ++ -- MS -- MS -- ++ ++ --
    -- ++ ME -- -- __ -- -- ME ++ --
    Me -- -- ++ ++ -- ++ ++ -- -- Me
    ++ ME -- ++ MS -- MS ++ -- ME ++
    ++ ME -- -- -- MB -- -- -- ME ++
    -- -- ++ Me -- -- -- Me ++ -- --
    -- ++ ++ ++ SP -- SP ++ ++ ++ --
    ++ -- -- ++ ++ -- ++ ++ -- -- ++
    -- -- -- ++ ++ -- ++ ++ -- -- --
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 2},
    {'battle': 5, 'enemy': 1, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, K6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, J7, K7, \
A8, B8, C8, D8, E8, F8, G8, H8, I8, J8, K8, \
A9, B9, C9, D9, E9, F9, G9, H9, I9, J9, K9, \
A10, B10, C10, D10, E10, F10, G10, H10, I10, J10, K10, \
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['CA', 'SS']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_AMBUSH = False
    # ===== End of generated config =====

    MAP_SWIPE_MULTIPLY_MINITOUCH = 1.446
    MAP_SWIPE_MULTIPLY = 1.495


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True
        if self.clear_enemy(scale=(2,)):
            return True
        if self.clear_enemy(scale=(1,)):
            return True

        return self.battle_default()

    def battle_5(self):
        return self.fleet_boss.clear_boss()
