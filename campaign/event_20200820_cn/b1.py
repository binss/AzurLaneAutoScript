from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

MAP = CampaignMap('B1')
MAP.shape = 'I7'
MAP.camera_data = ['D2', 'D5', 'F2', 'F5']
MAP.camera_data_spawn_point = ['D5']
MAP.map_covered = ['D1']
MAP.map_data = """
    MB -- -- MS -- -- -- -- --
    -- ME -- ++ ++ ME ++ ++ --
    -- -- __ ++ ++ -- MB ++ --
    MS ME -- -- -- -- -- Me --
    -- -- MS -- ME Me -- -- ME
    -- ++ -- -- -- -- ME ++ --
    -- ++ SP SP -- ME -- ++ --
"""
MAP.weight_data = """
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
    10 10 10 10 10 10 10 10 10
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 1},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    # Extract: {'battle': 4, 'enemy': 2, 'boss': 1},
    {'battle': 4, 'enemy': 1, 'boss': 1},
    {'battle': 5, 'enemy': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, \
A7, B7, C7, D7, E7, F7, G7, H7, I7, \
    = MAP.flatten()


class Config:
    MAP_SIREN_TEMPLATE = ['CL']
    MOVABLE_ENEMY_TURN = (2,)
    MAP_HAS_SIREN = True
    MAP_HAS_MAP_STORY = True
    MAP_HAS_FLEET_STEP = True

    MAP_HAS_AMBUSH = False
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_SWIPE_MULTIPLY = 1.694


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True

        return self.battle_default()

    def battle_4(self):
        return self.fleet_1.clear_boss()
