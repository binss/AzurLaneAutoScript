import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_SuccessInterval = 0
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '00:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'auto'  # auto, com.bilibili.azurlane, com.YoStarEN.AzurLane, com.YoStarJP.AzurLane, com.hkmanjuu.azurlane.gp, com.bilibili.blhx.huawei, com.bilibili.blhx.mi, com.tencent.tmgp.bilibili.blhx, com.bilibili.blhx.baidu, com.bilibili.blhx.qihoo, com.bilibili.blhx.oppo, com.bilibili.blhx.vivo, com.bilibili.blhx.uc, com.bilibili.blhx.mzw, com.yiwu.blhx.yx15, com.hkmanjuu.azurlane.gp.mc
    Emulator_ScreenshotMethod = 'ADB'  # ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc
    Emulator_ControlMethod = 'minitouch'  # ADB, uiautomator2, minitouch, Hermit
    Emulator_ScreenshotDedithering = False

    # Group `Error`
    Error_HandleError = True
    Error_SaveError = True
    Error_ScreenshotLength = 1

    # Group `Optimization`
    Optimization_ScreenshotInterval = 0.3
    Optimization_CombatScreenshotInterval = 1.0
    Optimization_TaskHoardingDuration = 0
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game

    # Group `DropRecord`
    DropRecord_SaveFolder = './screenshots'
    DropRecord_AzurStatsID = None
    DropRecord_SaveResearch = False
    DropRecord_UploadResearch = False
    DropRecord_SaveCommission = False
    DropRecord_UploadCommission = False
    DropRecord_SaveCombat = False
    DropRecord_SaveOpsi = False
    DropRecord_UploadOpsi = False
    DropRecord_SaveMeowfficer = False
    DropRecord_SaveMeowfficerTalent = False
    DropRecord_UploadMeowfficerTalent = False

    # Group `Retirement`
    Retirement_Enable = True
    Retirement_RetireMode = 'one_click_retire'  # one_click_retire, enhance, old_retire
    Retirement_RetireAmount = 'retire_all'  # retire_all, retire_10
    Retirement_EnhanceFavourite = False
    Retirement_EnhanceFilter = None
    Retirement_EnhanceCheckPerCategory = 2
    Retirement_OldRetireN = True
    Retirement_OldRetireR = True
    Retirement_OldRetireSR = False
    Retirement_OldRetireSSR = False

    # Group `Campaign`
    Campaign_Name = '12-4'
    Campaign_Event = 'campaign_main'  # campaign_main
    Campaign_Mode = 'normal'  # normal, hard
    Campaign_UseClearMode = True
    Campaign_UseFleetLock = True
    Campaign_UseAutoSearch = True
    Campaign_Use2xBook = False
    Campaign_AmbushEvade = True

    # Group `StopCondition`
    StopCondition_RunCount = 0
    StopCondition_OilLimit = 1000
    StopCondition_MapAchievement = 'non_stop'  # non_stop, 100_percent_clear, map_3_stars, threat_safe, threat_safe_without_3_stars
    StopCondition_StageIncrease = False
    StopCondition_GetNewShip = False
    StopCondition_ReachLevel = 0

    # Group `Fleet`
    Fleet_Fleet1 = 1  # 1, 2, 3, 4, 5, 6
    Fleet_Fleet1Formation = 'double_line'  # line_ahead, double_line, diamond
    Fleet_Fleet1Mode = 'combat_auto'  # combat_auto, combat_manual, stand_still_in_the_middle, hide_in_bottom_left
    Fleet_Fleet1Step = 3  # 2, 3, 4, 5
    Fleet_Fleet2 = 2  # 0, 1, 2, 3, 4, 5, 6
    Fleet_Fleet2Formation = 'double_line'  # line_ahead, double_line, diamond
    Fleet_Fleet2Mode = 'combat_auto'  # combat_auto, combat_manual, stand_still_in_the_middle, hide_in_bottom_left
    Fleet_Fleet2Step = 2  # 2, 3, 4, 5
    Fleet_FleetOrder = 'fleet1_mob_fleet2_boss'  # fleet1_mob_fleet2_boss, fleet1_boss_fleet2_mob, fleet1_all_fleet2_standby, fleet1_standby_fleet2_all

    # Group `Submarine`
    Submarine_Fleet = 0  # 0, 1, 2
    Submarine_Mode = 'do_not_use'  # do_not_use, hunt_only, boss_only, every_combat
    Submarine_AutoSearchMode = 'sub_standby'  # sub_standby, sub_auto_call
    Submarine_DistanceToBoss = '2_grid_to_boss'  # to_boss_position, 1_grid_to_boss, 2_grid_to_boss, use_U522_skill

    # Group `Emotion`
    Emotion_CalculateEmotion = True
    Emotion_IgnoreLowEmotionWarn = False
    Emotion_Fleet1Value = 119
    Emotion_Fleet1Record = datetime.datetime(2020, 1, 1, 0, 0)
    Emotion_Fleet1Control = 'prevent_yellow_face'  # keep_exp_bonus, prevent_green_face, prevent_yellow_face, prevent_red_face
    Emotion_Fleet1Recover = 'not_in_dormitory'  # not_in_dormitory, dormitory_floor_1, dormitory_floor_2
    Emotion_Fleet1Oath = False
    Emotion_Fleet2Value = 119
    Emotion_Fleet2Record = datetime.datetime(2020, 1, 1, 0, 0)
    Emotion_Fleet2Control = 'prevent_yellow_face'  # keep_exp_bonus, prevent_green_face, prevent_yellow_face, prevent_red_face
    Emotion_Fleet2Recover = 'not_in_dormitory'  # not_in_dormitory, dormitory_floor_1, dormitory_floor_2
    Emotion_Fleet2Oath = False

    # Group `HpControl`
    HpControl_UseHpBalance = False
    HpControl_UseEmergencyRepair = False
    HpControl_UseLowHpRetreat = False
    HpControl_HpBalanceThreshold = 0.2
    HpControl_HpBalanceWeight = '1000, 1000, 1000'
    HpControl_RepairUseSingleThreshold = 0.3
    HpControl_RepairUseMultiThreshold = 0.6
    HpControl_LowHpRetreatThreshold = 0.3

    # Group `EnemyPriority`
    EnemyPriority_EnemyScaleBalanceWeight = 'default_mode'  # default_mode, S3_enemy_first, S1_enemy_first

    # Group `C11AffinityFarming`
    C11AffinityFarming_RunCount = 32

    # Group `C72MysteryFarming`
    C72MysteryFarming_StepOnA3 = True

    # Group `C122MediumLeveling`
    C122MediumLeveling_LargeEnemyTolerance = 1  # 0, 1, 2, 10

    # Group `C124LargeLeveling`
    C124LargeLeveling_NonLargeEnterTolerance = 1  # 0, 1, 2
    C124LargeLeveling_NonLargeRetreatTolerance = 1  # 0, 1, 2, 10
    C124LargeLeveling_PickupAmmo = 3  # 3, 4, 5

    # Group `GemsFarming`
    GemsFarming_FlagshipChange = True
    GemsFarming_FlagshipEquipChange = False
    GemsFarming_VanguardChange = False
    GemsFarming_VanguardEquipChange = False
    GemsFarming_LowEmotionRetreat = True
    GemsFarming_CommonCV = 'any'  # any, langley, bogue, ranger, hermes

    # Group `EventGeneral`
    EventGeneral_PtLimit = 0
    EventGeneral_TimeLimit = datetime.datetime(2020, 1, 1, 0, 0)

    # Group `EventAb`
    EventAb_StageFilter = 'A1 > A2 > A3 > B1 > B2 > B3'
    EventAb_LastStage = 0

    # Group `EventCd`
    EventCd_StageFilter = 'C1 > C2 > C3 > D1 > D2 > D3'
    EventCd_LastStage = 0

    # Group `Raid`
    Raid_Mode = 'hard'  # easy, normal, hard
    Raid_UseTicket = False

    # Group `RaidDaily`
    RaidDaily_StageFilter = 'hard > normal > easy'

    # Group `MaritimeEscort`
    MaritimeEscort_Enable = True

    # Group `Commission`
    Commission_DoMajorCommission = False
    Commission_CommissionFilter = 'DailyEvent\n> Gem-8 > Gem-4 > Gem-2\n> NightDrill-8 > NightDrill-7 > NightDrill-6\n> ExtraDrill-0:20 > ExtraDrill-1 > ExtraDrill-2 > ExtraDrill-2:40 > ExtraDrill-3:20 > ExtraDrill-5:20\n> Box-6 > Box-3 > Box-1\n> DailyCube-0:30 > UrgentCube-1:30 > DailyCube-1:30 > UrgentCube-1:45 > UrgentCube-2:15 > UrgentCube-3\n> Major\n> DailyChip > DailyResource\n> UrgentBook-2:30 > UrgentBook-2 > UrgentBook-1:20 > UrgentBook-1:40\n> Daily-0:20 > Daily-0:30 > Daily-1:00 > Daily-1:30 > Daily-2:00\n> NightOil > NightCube\n> shortest'

    # Group `Tactical`
    Tactical_TacticalFilter = 'SameT4 > SameT3 > SameT2 > SameT1\n> BlueT2 > YellowT2 > RedT2\n> BlueT3 > YellowT3 > RedT3\n> BlueT4 > YellowT4 > RedT4\n> BlueT1 > YellowT1 > RedT1\n> first'

    # Group `ControlExpOverflow`
    ControlExpOverflow_Enable = True
    ControlExpOverflow_T4Allow = 100
    ControlExpOverflow_T3Allow = 100
    ControlExpOverflow_T2Allow = 200
    ControlExpOverflow_T1Allow = 200

    # Group `Research`
    Research_UseCube = 'only_05_hour'  # always_use, only_05_hour, only_no_project, do_not_use
    Research_UseCoin = 'always_use'  # always_use, only_05_hour, only_no_project, do_not_use
    Research_UsePart = 'always_use'  # always_use, only_05_hour, only_no_project, do_not_use
    Research_PresetFilter = 'series_4_blueprint_tenrai'  # custom, series_4_blueprint_tenrai, series_4_blueprint_only, series_4_tenrai_only, series_3, series_3_than_2
    Research_CustomFilter = 'S4-Q0.5 > Q-0.5 > S4-DR0.5 > S4-PRY0.5 > DR-0.5 > PRY-0.5\n> S4-Q1 > S4-Q2\n> S4-DR2.5 > S4-G1.5\n> S4-Q4 > S4-H0.5 > S4-G4\n> S4-PRY2.5 > S4-G2.5\n> reset > S4-H1 > shortest'

    # Group `Dorm`
    Dorm_Collect = True
    Dorm_Feed = True
    Dorm_FeedFilter = '20000 > 10000 > 5000 > 3000 > 2000 > 1000'

    # Group `Meowfficer`
    Meowfficer_BuyAmount = 1
    Meowfficer_FortChoreMeowfficer = True

    # Group `MeowfficerTrain`
    MeowfficerTrain_Enable = False
    MeowfficerTrain_Mode = 'seamlessly'  # seamlessly, once_a_day
    MeowfficerTrain_RetainTalentedGold = True
    MeowfficerTrain_RetainTalentedPurple = True
    MeowfficerTrain_EnhanceIndex = 1

    # Group `GuildLogistics`
    GuildLogistics_Enable = True
    GuildLogistics_SelectNewMission = False
    GuildLogistics_ExchangeFilter = 'PlateTorpedoT1 > PlateAntiAirT1 > PlatePlaneT1 > PlateGunT1 > PlateGeneralT1\n> PlateTorpedoT2 > PlateAntiAirT2 > PlatePlaneT2 > PlateGunT2 > PlateGeneralT2\n> PlateTorpedoT3 > PlateAntiAirT3 > PlatePlaneT3 > PlateGunT3 > PlateGeneralT3\n> OxyCola > Coolant > Merit > Coin > Oil'

    # Group `GuildOperation`
    GuildOperation_Enable = True
    GuildOperation_SelectNewOperation = False
    GuildOperation_NewOperationMaxDate = 15
    GuildOperation_JoinThreshold = 1
    GuildOperation_AttackBoss = True
    GuildOperation_BossFleetRecommend = False

    # Group `Reward`
    Reward_CollectOil = True
    Reward_CollectCoin = True
    Reward_CollectExp = True
    Reward_CollectMission = True
    Reward_CollectWeeklyMission = True

    # Group `GeneralShop`
    GeneralShop_UseGems = False
    GeneralShop_Refresh = False
    GeneralShop_BuySkinBox = False
    GeneralShop_Filter = 'BookRedT3 > BookYellowT3 > BookBlueT3 > BookRedT2\n> Cube\n> FoodT6 > FoodT5'

    # Group `GuildShop`
    GuildShop_Refresh = True
    GuildShop_Filter = 'PlateT4 > BookT3 > PR > CatT3 > Chip > BookT2 > Retrofit > FoodT6 > FoodT5 > CatT2 > BoxT4'
    GuildShop_BOX_T3 = 'ironblood'  # eagle, royal, sakura, ironblood
    GuildShop_BOX_T4 = 'ironblood'  # eagle, royal, sakura, ironblood
    GuildShop_BOOK_T2 = 'red'  # red, blue, yellow
    GuildShop_BOOK_T3 = 'red'  # red, blue, yellow
    GuildShop_RETROFIT_T2 = 'cl'  # dd, cl, bb, cv
    GuildShop_RETROFIT_T3 = 'cl'  # dd, cl, bb, cv
    GuildShop_PLATE_T2 = 'general'  # general, gun, torpedo, antiair, plane
    GuildShop_PLATE_T3 = 'general'  # general, gun, torpedo, antiair, plane
    GuildShop_PLATE_T4 = 'gun'  # general, gun, torpedo, antiair, plane
    GuildShop_PR1 = 'neptune'  # neptune, monarch, ibuki, izumo, roon, saintlouis
    GuildShop_PR2 = 'seattle'  # seattle, georgia, kitakaze, gascogne
    GuildShop_PR3 = 'cheshire'  # cheshire, mainz, odin, champagne

    # Group `MedalShop`
    MedalShop_Filter = 'DR > PR\n> BookRedT3 > BookYellowT3 > BookBlueT3 > BookRedT2 > BookYellowT2 > BookBlueT2\n> RetrofitT3 > PlateGeneralT3\n> FoodT6 > FoodT5'

    # Group `MeritShop`
    MeritShop_Refresh = False
    MeritShop_Filter = 'Cube'

    # Group `CoreShop`
    CoreShop_Filter = 'Array'

    # Group `Shipyard`
    Shipyard_ResearchSeries = 1
    Shipyard_ShipIndex = 0
    Shipyard_BuyAmount = 2

    # Group `Gacha`
    Gacha_Pool = 'light'  # light, heavy, special, event, wishing_well
    Gacha_Amount = 1  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    Gacha_UseDrill = False

    # Group `SupplyPack`
    SupplyPack_WeeklyFreeSupplyPack = True

    # Group `BattlePass`
    BattlePass_BattlePassReward = True

    # Group `MetaReward`
    MetaReward_MetaReward = True

    # Group `Daily`
    Daily_UseDailySkip = True
    Daily_EscortMission = 'first'  # skip, first, second, third
    Daily_EscortMissionFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_AdvanceMission = 'first'  # skip, first, second, third
    Daily_AdvanceMissionFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_FierceAssault = 'first'  # skip, first, second, third
    Daily_FierceAssaultFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_TacticalTraining = 'second'  # skip, first, second, third
    Daily_TacticalTrainingFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_SupplyLineDisruption = 'second'  # skip, first, second, third

    # Group `Hard`
    Hard_HardStage = '11-4'
    Hard_HardFleet = 1  # 1, 2

    # Group `Exercise`
    Exercise_OpponentChooseMode = 'max_exp'  # max_exp, easiest, leftmost, easiest_else_exp
    Exercise_OpponentTrial = 1
    Exercise_ExercisePreserve = 0
    Exercise_LowHpThreshold = 0.4
    Exercise_LowHpConfirmWait = 0.1
    Exercise_OpponentRefreshValue = 0
    Exercise_OpponentRefreshRecord = datetime.datetime(2020, 1, 1, 0, 0)

    # Group `Sos`
    Sos_Chapter = 3  # 3, 4, 5, 6, 7, 8, 9, 10

    # Group `OpsiAshAssist`
    OpsiAshAssist_Tier = 15

    # Group `OpsiGeneral`
    OpsiGeneral_UseLogger = True
    OpsiGeneral_BuyActionPoint = False
    OpsiGeneral_OilLimit = 1000
    OpsiGeneral_RepairThreshold = 0.4
    OpsiGeneral_DoRandomMapEvent = True
    OpsiGeneral_AkashiShopFilter = 'ActionPoint > PurpleCoins'

    # Group `OpsiAshBeacon`
    OpsiAshBeacon_AshAttack = True
    OpsiAshBeacon_EnsureFullyCollected = True
    OpsiAshBeacon_RequestAssist = True

    # Group `OpsiFleetFilter`
    OpsiFleetFilter_Filter = 'Fleet-4 > CallSubmarine > Fleet-2 > Fleet-3 > Fleet-1'

    # Group `OpsiFleet`
    OpsiFleet_Fleet = 1  # 1, 2, 3, 4
    OpsiFleet_Submarine = False

    # Group `OpsiExplore`
    OpsiExplore_SpecialRadar = False
    OpsiExplore_ForceRun = False
    OpsiExplore_LastZone = 0

    # Group `OpsiShop`
    OpsiShop_BuySupply = True

    # Group `OpsiDaily`
    OpsiDaily_DoMission = True
    OpsiDaily_UseTuningSample = True

    # Group `OpsiObscure`
    OpsiObscure_ForceRun = False

    # Group `OpsiAbyssal`
    OpsiAbyssal_ForceRun = False

    # Group `OpsiStronghold`
    OpsiStronghold_ForceRun = False

    # Group `OpsiMeowfficerFarming`
    OpsiMeowfficerFarming_ActionPointPreserve = 500
    OpsiMeowfficerFarming_HazardLevel = 5  # 3, 4, 5, 6, 10
    OpsiMeowfficerFarming_TargetZone = 0

    # Group `Daemon`
    Daemon_EnterMap = True

    # Group `OpsiDaemon`
    OpsiDaemon_RepairShip = True
    OpsiDaemon_SelectEnemy = True

    # Group `Benchmark`
    Benchmark_AdbScreenshot = True
    Benchmark_AdbncScreenshot = True
    Benchmark_Uiautomator2Screenshot = True
    Benchmark_AscreencapScreenshot = True
    Benchmark_AscreencapncScreenshot = True
    Benchmark_AdbClick = True
    Benchmark_Uiautomator2Click = True
    Benchmark_MinitouchClick = True
    Benchmark_HermitClick = False

    # Group `AzurLaneUncensored`
    AzurLaneUncensored_Repository = 'https://gitee.com/LmeSzinc/AzurLaneUncensored'

    # Group `GameManager`
    GameManager_AutoRestart = True
