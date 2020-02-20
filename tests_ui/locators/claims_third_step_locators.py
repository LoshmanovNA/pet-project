
class ClaimsThirdStepLocators:
    """Третий шаг подачи заявки (Новое присоединение)"""
    # Блок "Энергопринимющие устройства"
    THIRD_STEP_EPU_TYPE_DROPDOWN_CSS = '.epu_epu_type > .custom-combobox > a'  # Наименование ЭПУ (открыть список)
    THIRD_STEP_EPU_TYPES_LIST_CSS = '.epu_epu_type ul li:nth-child(2)'  # Первое значение в списке
    THIRD_STEP_CADASTRAL_YES_CSS = '#cadastral_availability_yes'  # Кадастровый номер есть (радиобатон)
    THIRD_STEP_CADASTRAL_NO_CSS = '#cadastral_availability_no'  # Кадастровый номер отсутствует (радиобатон)
    THIRD_STEP_INPUT_CADASTRAL_CSS = '#epu_cadastral_number'  # Поле ввода кадастрового номера
    THIRD_STEP_FIND_CADASTRAL_BUTTON_CSS = '#find-adds'  # Кнопка поиска адреса на Росреестре
    THIRD_STEP_CUSTOM_ADDRESS_CHECKBOX_CSS = '#epu_custom_address_toggler'  # Чек-бокс "Указать адрес в
    # произвольной форме"
    THIRD_STEP_EPU_FULL_ADDRESS_CSS = '#epu_fias_full_address'  # Поле ввода полного адреса
    THIRD_STEP_EPU_REGION_CSS = '#epu_region ~ a'  # Раскрыть список значений региона
    THIRD_STEP_EPU_AREA_CSS = '#epu_area ~ a'  # Раскрыть список значений района
    THIRD_STEP_EPU_CITY_CSS = '#epu_city ~ a'  # Раскрыть список значений города
    THIRD_STEP_EPU_SETTLEMENT_CSS = '#epu_settlement ~ a'  # Раскрыть список значений
    # населенных пунктов
    THIRD_STEP_EPU_STREET_CSS = '#epu_street ~ a'  # Раскрыть список значений улиц
    THIRD_STEP_EPU_HOUSE_CSS = '#epu_house'  # Поле ввода номера дома
    THIRD_STEP_EPU_CORPS_CSS = '#epu_corps'  # Поле ввода номера корпуса
    THIRD_STEP_EPU_BUILDING_CSS = '#epu_building'  # Поле ввода номера строения
    THIRD_STEP_EPU_INDEX_CSS = '#epu_postcode'  # Поле ввода номера индекса

    # Блок "Мощность и напряжение"
    THIRD_STEP_MAX_POWER_CSS = '#epu_max_power'  # Ввод максимальной мощности для присоединения
    THIRD_STEP_VOLTAGE_LIST_CSS = 'div.epu_voltage_level span  a'  # Раскрыть список классов напряжения
    THIRD_STEP_VOLTAGE_VALUE_XPATH = '//div[text()="380 вольт"]'  # Выбор значения напряжения
    # Блок категории надежности при мощности до 150 кВт
    THIRD_STEP_RELIABILITY_LIST_CSS = '.epu_reliability_level span a'  # Раскрыть список категорий надежности
    THIRD_STEP_RELIABILITY_VALUE_XPATH = '//div[text()="3"]'  # Выбор значения категории надежности
    # Блок категории надежности при мощности свыше 150 кВт
    THIRD_STEP_RELIABILITY_INPUT_XPATH = '//input[@id="3"]'  # Выбор значения категории надежности

    # Блок "Количество точек присоединения"
    THIRD_STEP_EPU_POINTS_CSS = '#epu_point_count'  # Ввод количества точек присоединения
    THIRD_STEP_EPU_POINTS_INFO_CSS = '#point_count_info'  # Инфоблок при количестве точек более 4
    THIRD_STEP_EPU_POINT1_DESCRIBE_CSS = 'input[name="connection_point[0][name]"]'  # Описание точки 1
    THIRD_STEP_EPU_POINT2_DESCRIBE_CSS = 'input[name="connection_point[1][name]"]'  # Описание точки 2
    THIRD_STEP_EPU_POINT1_POWER_CSS = 'input[name="connection_point[0][power]"]'  # Мощность точки 1
    THIRD_STEP_EPU_POINT2_POWER_CSS = 'input[name="connection_point[1][power]"]'  # Мощность точки 2

# Блок количества и мощности трансформаторов