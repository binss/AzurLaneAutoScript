from typing import List, Tuple
from module.base.button import ButtonGrid
from module.base.timer import Timer
from module.logger import logger
from module.meowfficer.assets import *
from module.meowfficer.base import MeowfficerBase
from module.ui.switch import Switch

MEOWFFICER_TALENT_GRID_1 = ButtonGrid(
    origin=(875, 559), delta=(105, 0), button_shape=(16, 16), grid_shape=(3, 1),
    name='MEOWFFICER_TALENT_GRID_1')
MEOWFFICER_TALENT_GRID_2 = MEOWFFICER_TALENT_GRID_1.move(vector=(-40, -20),
                                                         name='MEOWFFICER_TALENT_GRID_2')
MEOWFFICER_SHIFT_DETECT = Button(
    area=(1260, 669, 1280, 720), color=(117, 106, 84), button=(1260, 669, 1280, 720),
    name='MEOWFFICER_SHIFT_DETECT')

SWITCH_LOCK = Switch(name='Meowfficer_Lock', offset=(40, 40))
SWITCH_LOCK.add_status(
    'lock',
    check_button=MEOWFFICER_APPLY_UNLOCK,
    click_button=MEOWFFICER_APPLY_LOCK
)
SWITCH_LOCK.add_status(
    'unlock',
    check_button=MEOWFFICER_APPLY_LOCK,
    click_button=MEOWFFICER_APPLY_UNLOCK
)


class MeowfficerCollect(MeowfficerBase):
    def _meow_detect_shift(self, skip_first_screenshot=True):
        """
        Serves as innate wait mechanism for loading
        of meowfficer acquisition complete screen
        During which screen may shift left randomly

        Args:
            skip_first_screenshot (bool):

        Returns:
            bool
        """
        flag = False
        confirm_timer = Timer(3, count=6).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            # End - Random left shift
            if self.image_color_count(MEOWFFICER_SHIFT_DETECT,
                                      color=MEOWFFICER_SHIFT_DETECT.color, threshold=221, count=650):
                if not flag:
                    confirm_timer.reset()
                    flag = True
                if confirm_timer.reached():
                    break
                continue

            # End - No shift at all
            if self.appear(MEOWFFICER_GET_CHECK, offset=(40, 40)):
                if flag:
                    confirm_timer.reset()
                    flag = False
                if confirm_timer.reached():
                    break
        return flag

    def _get_meow_talent_grid(self) -> Tuple[List[Button], bool]:
        """
            get meow talent grid list and special talent status
        Returns:
           Tuple[List[ButtonGrid], bool]
        """
        # Wait for complete load before examining talents
        logger.info('Configured to retain this type of meowfficer, '
                    'wait complete load and examine base talents')

        list_talent_grid = []
        special_talent = False
        grid = MEOWFFICER_TALENT_GRID_2 if self._meow_detect_shift() else MEOWFFICER_TALENT_GRID_1

        for btn in grid.buttons:
            # Empty slot; check for many white pixels
            if self.image_color_count(btn, color=(255, 255, 247), threshold=221, count=200):
                continue

            # Non-empty slot; check for few white pixels
            # i.e. roman numerals
            if self.image_color_count(btn, color=(255, 255, 255), threshold=221, count=25):
                list_talent_grid.append(btn)
                continue

            # Detected special talent
            list_talent_grid.append(btn)
            special_talent = True

        logger.info('At least one special talent ability detected') if special_talent else \
            logger.info('No special talent abilities detected')
        return list_talent_grid, special_talent

    def _meow_talent_cap_handle(self, talent_button: List[Button], drop):
        for btn in talent_button:
            self.ui_click(btn, check_button=MEOWFFICER_TALENT_CLOSE,
                          appear_button=MEOWFFICER_GET_CHECK, skip_first_screenshot=True)
            drop.add(self.device.image)
            self.ui_click(MEOWFFICER_TALENT_CLOSE, check_button=self._check_popup_exit,
                          appear_button=MEOWFFICER_TALENT_CLOSE, skip_first_screenshot=True)
            self.device.click_record.pop()
            self.device.click_record.pop()

    def _meow_apply_lock(self, lock=True):
        """
        Apply designated lock status onto
        the acquired trained meowfficer
        Prevents the meowfficer being used
        as feed / enhance material

        Args:
            lock (bool):
        """
        # Apply designated lock status
        SWITCH_LOCK.set(status='lock' if lock else 'unlock', main=self)

        # Wait until info bar disappears
        self.ensure_no_info_bar(timeout=1)

    # Transition out of lock popup / talent detail panel
    # Use callable as screen is variable
    def _check_popup_exit(self):
        """
        Returns: boll
        """
        if self.appear(MEOWFFICER_GET_CHECK, offset=(40, 40)) and MEOWFFICER_GET_CHECK.match_appear_on(
                self.device.image):
            return True

        if self.appear(MEOWFFICER_TRAIN_START, offset=(20, 20)):
            return True

        return False

    def _meow_skip_lock(self):
        """
        Applicable to only gold variant meowfficer
        Handle skip transitions; proceeds slowly
        with caution to prevent unintentional actions
        """
        # Trigger lock popup appearance to initiate sequence
        self.ui_click(MEOWFFICER_TRAIN_CLICK_SAFE_AREA,
                      appear_button=MEOWFFICER_GET_CHECK, check_button=MEOWFFICER_CONFIRM,
                      offset=(40, 40), retry_wait=3, skip_first_screenshot=True)

        self.ui_click(MEOWFFICER_CANCEL, check_button=self._check_popup_exit,
                      offset=(40, 20), retry_wait=3, skip_first_screenshot=True)
        self.device.click_record.pop()
        self.device.click_record.pop()

    def meow_get(self, skip_first_screenshot=True):
        """
        Transition through all the necessary screens
        to acquire each trained meowfficer
        Animation is waited for as the amount can vary
        Only gold variant meowfficer will prompt for
        confirmation

        Args:
            skip_first_screenshot (bool): Skip first
            screen shot or not

        Pages:
            in: MEOWFFICER_GET_CHECK
            out: MEOWFFICER_TRAIN
        """
        # Loop through possible screen transitions
        confirm_timer = Timer(1.5, count=3).start()
        count = 0
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.handle_meow_popup_dismiss():
                confirm_timer.reset()
                continue
            if self.appear(MEOWFFICER_GET_CHECK, offset=(40, 40), interval=3):
                count += 1
                logger.attr('Meow_get', count)
                with self.stat.new(
                        genre="meowfficer_talent",
                        upload=self.config.DropRecord_UploadMeowfficerTalent,
                        save=self.config.DropRecord_SaveMeowfficerTalent,
                ) as drop:
                    drop.add(self.device.image)
                    list_talent_btn, special_talent = self._get_meow_talent_grid()
                    self._meow_talent_cap_handle(list_talent_btn, drop)
                    if self.appear(MEOWFFICER_GOLD_CHECK, offset=(40, 40)):
                        if not self.config.MeowfficerTrain_RetainTalentedGold or not special_talent:
                            self._meow_skip_lock()
                            skip_first_screenshot = True
                            confirm_timer.reset()
                            continue
                        self._meow_apply_lock()

                    if self.appear(MEOWFFICER_PURPLE_CHECK, offset=(40, 40)):
                        if self.config.MeowfficerTrain_RetainTalentedPurple and special_talent:
                            self._meow_apply_lock()

                    # Susceptible to exception when collecting multiple
                    # Mitigate by popping click_record
                    self.device.click(MEOWFFICER_TRAIN_CLICK_SAFE_AREA)
                    self.device.click_record.pop()
                    confirm_timer.reset()
                    self.interval_reset(MEOWFFICER_GET_CHECK)
                    continue

            # End
            if self.appear(MEOWFFICER_TRAIN_START, offset=(20, 20)):
                if confirm_timer.reached():
                    break
            else:
                confirm_timer.reset()

    def meow_collect(self, collect_all=True):
        """
        Collect one or all trained meowfficer(s)
        Completed slots are automatically moved
        to top of queue, assume to check top-left
        slot only

        Args:
            collect_all (bool): Collect all or collect single

        Pages:
            in: MEOWFFICER_TRAIN
            out: MEOWFFICER_TRAIN

        Returns:
            bool: whether collected or not
        """
        logger.hr('Meowfficer collect', level=2)

        if self.appear(MEOWFFICER_TRAIN_COMPLETE, offset=(20, 20)):
            # Today is Sunday, finish all else get just one
            if collect_all:
                logger.info('Collect all trained meowfficers')
                button = MEOWFFICER_TRAIN_FINISH_ALL
            else:
                logger.info('Collect single trained meowfficer')
                button = MEOWFFICER_TRAIN_COMPLETE
            self.ui_click(button, check_button=MEOWFFICER_GET_CHECK,
                          additional=self.handle_meow_popup_dismiss,
                          offset=(40, 40), skip_first_screenshot=True)

            # Get loop mechanism to collect trained meowfficer(s)
            self.meow_get()
            return True
        return False
