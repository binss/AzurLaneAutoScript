from module.base.button import ButtonGrid
from module.base.timer import Timer
from module.base.utils import color_similar, get_color, resize
from module.combat.assets import GET_ITEMS_1
from module.exception import RequestHumanTakeover, ScriptError
from module.logger import logger
from module.retire.assets import *
from module.retire.enhancement import Enhancement

CARD_GRIDS = ButtonGrid(
    origin=(93, 76), delta=(164 + 2 / 3, 227), button_shape=(138, 204), grid_shape=(7, 2), name='CARD')
CARD_RARITY_GRIDS = ButtonGrid(
    origin=(93, 76), delta=(164 + 2 / 3, 227), button_shape=(138, 5), grid_shape=(7, 2), name='RARITY')

CARD_RARITY_COLORS = {
    'N': (174, 176, 187),
    'R': (106, 195, 248),
    'SR': (151, 134, 254),
    'SSR': (248, 223, 107)
    # Not support marriage cards.
}


class Retirement(Enhancement):
    _unable_to_enhance = False
    _have_keeped_cv = True

    def _retirement_choose(self, amount=10, target_rarity=('N',)):
        """
        Args:
            amount (int): Amount of cards retire. 0 to 10.
            target_rarity (tuple(str)): Card rarity. N, R, SR, SSR.

        Returns:
            int: Amount of cards have retired.
        """
        cards = []
        rarity = []
        for x, y, button in CARD_RARITY_GRIDS.generate():
            card_color = get_color(image=self.device.image, area=button.area)
            f = False
            for r, rarity_color in CARD_RARITY_COLORS.items():

                if color_similar(card_color, rarity_color, threshold=15):
                    cards.append([x, y])
                    rarity.append(r)
                    f = True

            if not f:
                logger.warning(
                    f'Unknown rarity color. Grid: ({x}, {y}). Color: {card_color}')

        logger.info(' '.join([r.rjust(3) for r in rarity[:7]]))
        logger.info(' '.join([r.rjust(3) for r in rarity[7:]]))

        selected = 0
        for card, r in zip(cards, rarity):
            if r in target_rarity:
                self.device.click(CARD_GRIDS[card])
                self.device.sleep((0.1, 0.15))
                selected += 1
            if selected >= amount:
                break
        return selected

    def _retirement_confirm(self, skip_first_screenshot=True):
        """
        Pages:
            in: IN_RETIREMENT_CHECK, and also
                SHIP_CONFIRM_2 if using one_click_retire
                SHIP_CONFIRM if using old_retire
            out: IN_RETIREMENT_CHECK
        """
        executed = False
        backup, self._popup_offset = self._popup_offset, (20, 50)
        for button in [SHIP_CONFIRM, SHIP_CONFIRM_2, EQUIP_CONFIRM, EQUIP_CONFIRM_2, GET_ITEMS_1, SR_SSR_CONFIRM]:
            self.interval_clear(button)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            # End
            if executed and self.appear(IN_RETIREMENT_CHECK):
                self.handle_info_bar()
                break

            # Click
            if self.appear(SHIP_CONFIRM, offset=(30, 30), interval=2) \
                    and SHIP_CONFIRM.match_appear_on(self.device.image):
                self.device.click(SHIP_CONFIRM)
                continue
            if self.appear(SHIP_CONFIRM_2, offset=(30, 30), interval=2):
                if self.config.RETIRE_KEEP_COMMON_CV and not self._have_keeped_cv:
                    self.keep_one_common_cv()
                self.device.click(SHIP_CONFIRM_2)
                self.interval_clear(GET_ITEMS_1)
                continue
            if self.appear_then_click(EQUIP_CONFIRM, offset=(30, 30), interval=2):
                continue
            if self.appear_then_click(EQUIP_CONFIRM_2, offset=(30, 30), interval=2):
                self.interval_clear(GET_ITEMS_1)
                executed = True
                continue
            if self.appear(GET_ITEMS_1, offset=(30, 30), interval=2):
                self.device.click(GET_ITEMS_1_RETIREMENT_SAVE)
                self.interval_reset(SHIP_CONFIRM)
                continue
            if self._unable_to_enhance \
                    or self.config.Retirement_OldRetireSR \
                    or self.config.Retirement_OldRetireSSR \
                    or self.config.Retirement_RetireMode == 'one_click_retire':
                if self.handle_popup_confirm('RETIRE_SR_SSR'):
                    continue
                if self.config.SERVER in ['jp', 'tw'] and \
                        self.appear_then_click(SR_SSR_CONFIRM, offset=self._popup_offset, interval=2):
                    continue

        self._popup_offset = backup

    def retirement_appear(self):
        return self.appear(RETIRE_APPEAR_1, offset=30) \
            and self.appear(RETIRE_APPEAR_2, offset=30) \
            and self.appear(RETIRE_APPEAR_3, offset=30)

    def _retirement_quit(self):
        def check_func():
            return not self.appear(IN_RETIREMENT_CHECK) \
                and not self.appear(DOCK_CHECK)

        self.ui_back(check_button=check_func, skip_first_screenshot=True)

    @property
    def _retire_rarity(self):
        rarity = set()
        if self.config.Retirement_OldRetireN:
            rarity.add('N')
        if self.config.Retirement_OldRetireR:
            rarity.add('R')
        if self.config.Retirement_OldRetireSR:
            rarity.add('SR')
        if self.config.Retirement_OldRetireSSR:
            rarity.add('SSR')
        return rarity

    def retire_ships_one_click(self, amount=None):
        logger.hr('Retirement')
        logger.info('Using one click retirement.')
        self.dock_favourite_set(False)
        if amount is None:
            amount = self._retire_amount
        end = False
        total = 0

        if self.config.RETIRE_KEEP_COMMON_CV:
            self._have_keeped_cv = False

        while 1:
            self.handle_info_bar()

            skip_first_screenshot = True
            while 1:
                if skip_first_screenshot:
                    skip_first_screenshot = False
                else:
                    self.device.screenshot()
                # End
                if self.appear(SHIP_CONFIRM_2, offset=(30, 30)):
                    break
                if self.info_bar_count():
                    logger.info('No more ships to retire.')
                    end = True
                    break
                # Click
                if self.appear_then_click(ONE_CLICK_RETIREMENT, interval=2):
                    continue

            if end:
                break
            self._retirement_confirm()
            total += 10
            if total >= amount:
                break

        logger.info(f'Total retired round: {total // 10}')
        return total

    def retire_ships_old(self, amount=None, rarity=None):
        """
        Args:
            amount (int): Amount of cards retire. 0 to 2000.
            rarity (tuple(str)): Card rarity. N, R, SR, SSR.

        Returns:
            int: Total retired.
        """
        if amount is None:
            amount = self._retire_amount
        if rarity is None:
            rarity = self._retire_rarity
        logger.hr('Retirement')
        logger.info(f'Amount={amount}. Rarity={rarity}')

        # transfer N R SR SSR to filter name
        correspond_name = {
            'N': 'common',
            'R': 'rare',
            'SR': 'elite',
            'SSR': 'super_rare'
        }
        _rarity = [correspond_name[i] for i in rarity]
        self.dock_filter_set(sort='level', index='all',
                             faction='all', rarity=_rarity, extra='no_limit')
        self.dock_sort_method_dsc_set(False)
        self.dock_favourite_set(False)
        total = 0

        if self.config.RETIRE_KEEP_COMMON_CV:
            self._have_keeped_cv = False

        while amount:
            selected = self._retirement_choose(
                amount=10 if amount > 10 else amount, target_rarity=rarity)
            total += selected
            if selected == 0:
                break
            self.device.screenshot()
            if not (self.appear(SHIP_CONFIRM, offset=(30, 30)) and SHIP_CONFIRM.match_appear_on(self.device.image)):
                logger.warning('No ship selected, retrying')
                continue

            self._retirement_confirm()

            amount -= selected
            if amount <= 0:
                break

            self.handle_dock_cards_loading()
            continue

        self.dock_sort_method_dsc_set(True)
        self.dock_filter_set()
        logger.info(f'Total retired: {total}')
        return total

    def handle_retirement(self):
        """
        Returns:
            bool: If retired.
        """
        if not self.config.Retirement_Enable:
            return False

        if self._unable_to_enhance:
            if self.appear_then_click(RETIRE_APPEAR_1, offset=(20, 20), interval=3):
                self.interval_clear(IN_RETIREMENT_CHECK)
                return False
            if self.appear(IN_RETIREMENT_CHECK, offset=(20, 20), interval=10):
                self._retire_handler(mode='one_click_retire')
                self._unable_to_enhance = False
                self.interval_reset(IN_RETIREMENT_CHECK)
                return True
        elif self.config.Retirement_RetireMode == 'enhance':
            if self.appear_then_click(RETIRE_APPEAR_3, offset=(20, 20), interval=3):
                self.interval_clear(DOCK_CHECK)
                return False
            if self.appear(DOCK_CHECK, offset=(20, 20), interval=10):
                self.handle_dock_cards_loading()
                total, remain = self._enhance_handler()
                if not total:
                    logger.info(
                        'No ship to enhance, but dock full, will try retire')
                    self._unable_to_enhance = True
                logger.info(f'The remaining spare dock amount is {remain}')
                if remain < 3:
                    logger.info('Too few spare docks, retire next time')
                    self._unable_to_enhance = True
                self.interval_reset(DOCK_CHECK)
                return True
        else:
            if self.appear_then_click(RETIRE_APPEAR_1, offset=(20, 20), interval=3):
                self.interval_clear(IN_RETIREMENT_CHECK)
                return False
            if self.appear(IN_RETIREMENT_CHECK, offset=(20, 20), interval=10):
                self._retire_handler()
                self._unable_to_enhance = False
                self.interval_reset(IN_RETIREMENT_CHECK)
                return True

        return False

    def _retire_handler(self, mode=None):
        """
        Args:
            mode (str): `one_click_retire` or `old_retire`

        Returns:
            int: Amount of retired ships

        Pages:
            in: IN_RETIREMENT_CHECK
            out: the page before retirement popup
        """
        if mode is None:
            mode = self.config.Retirement_RetireMode

        if mode == 'one_click_retire':
            total = self.retire_ships_one_click()
            if not total:
                logger.warning(
                    'No ship retired, trying to reset dock filter and disable favourite, then retire again')
                self.dock_filter_set()
                self.dock_favourite_set(False)
                total = self.retire_ships_one_click()
            if not total:
                logger.critical('No ship retired')
                logger.critical('Please configure your one-click-retire in game, '
                                'make sure it can select ships to retire')
                raise RequestHumanTakeover
        elif mode == 'old_retire':
            self.handle_dock_cards_loading()
            total = self.retire_ships_old()
            if not total:
                logger.critical('No ship retired')
                logger.critical('Please configure your retirement settings in Alas, '
                                'make sure it can select ships to retire')
                raise RequestHumanTakeover
        else:
            raise ScriptError(
                f'Unknown retire mode: {self.config.Retirement_RetireMode}')

        self._retirement_quit()
        self.config.DOCK_FULL_TRIGGERED = True

        return total

    def _retire_select_one(self, button, skip_first_screenshot=True):
        """
        Args:
            button (Button): Ship button to select
            skip_first_screenshot:
        """

        retire_coin_timer = Timer(2)
        RETIRE_COIN.load_color(self.device.image)

        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()
            if self.appear(SHIP_CONFIRM_2, offset=(30, 30), interval=3):
                self.device.click(button)
                continue

            if retire_coin_timer.reached() and not self.appear(RETIRE_COIN, threshold=0.97):
                return True
        return False

    def retirement_get_common_rarity_cv(self):
        """
        Returns:
            Button:
        """
        if self.config.GemsFarming_CommonCV == 'any':
            for commen_cv_name in ['BOGUE', 'HERMES', 'LANGLEY', 'RANGER']:
                template = globals()[f'TEMPLATE_{commen_cv_name}']
                sim, button = template.match_result(
                    resize(self.device.image, size=(1189, 669)))

                if sim > self.config.COMMON_CV_THRESHOLD:
                    return Button(button=tuple(_ * 155 // 144 for _ in button.button), area=button.area,
                                  color=button.color,
                                  name=f'TEMPLATE_{commen_cv_name}_RETIRE')

                return None
        else:

            template = globals()[
                f'TEMPLATE_{self.config.GemsFarming_CommonCV.upper()}']
            sim, button = template.match_result(
                resize(self.device.image, size=(1189, 669)))

            if sim > self.config.COMMON_CV_THRESHOLD:
                return Button(button=tuple(_ * 155 // 144 for _ in button.button), area=button.area, color=button.color,
                              name=f'TEMPLATE_{self.config.GemsFarming_CommonCV.upper()}_RETIRE')

            return None

    def keep_one_common_cv(self):
        button = self.retirement_get_common_rarity_cv()
        if button is not None:
            self._retire_select_one(button, skip_first_screenshot=False)
            self._have_keeped_cv = True
