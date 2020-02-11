
class RegistrationPageLocators:
    """Страница регистрации"""
    #  Поля формы регистрации
    REGISTRATION_USER_TYPE_LIST_CSS = '.ui-autocomplete-input'
    REGISTRATION_USER_TYPE_FL_XPATH = '//li[contains(text(), "Физическое")]'
    REGISTRATION_USER_TYPE_UL_XPATH = '//li[contains(text(), "Юридическое")]'
    REGISTRATION_USER_TYPE_IP_XPATH = '//li[contains(text(), "Индивидуальный")]'
    REGISTRATION_USER_TYPE_PPD_XPATH = '//li[contains(text(), "Представитель")]'
    REGISTRATION_SURNAME_CSS = '#user_last_name'
    REGISTRATION_NAME_CSS = '#user_first_name'
    REGISTRATION_PATRONYMIC_CSS = '#user_patronymic_name'
    REGISTRATION_EMAIL_CSS = '#user_email'
    REGISTRATION_PHONE_CSS = '#phone_input'

    #  Чек-боксы согласия на странице регистрации
    REGISTRATION_CONFIRM1_CSS = '#confirm1'
    REGISTRATION_CONFIRM2_CSS = '#confirm2'
    REGISTRATION_CONFIRM3_CSS = '#confirm3'

    #  Кнопки "Продолжить регистрацию" и "Отмена"
    REGISTRATION_NEXT_STEP_CSS = '#nextStep'
    REGISTRATION_CLOSE_WINDOW_XPATH = '//a[contains(text(), "Закрыть")]'

    #  Ошибки валидации полей формы регистрации
    REGISTRATION_VALIDATION_ERROR_MESSAGES_XPATH = {
        'first_name': '//input[@id="user_first_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'last_name': '//input[@id="user_last_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'patronymic_name': '//input[@id="user_patronymic_name"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'phone': '//input[@id="phone_input"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'email': '//input[@id="user_email"]/ancestor::span[contains (@class, "invalid")]/following-sibling::div',
        'confirm_1': '//input[@id="confirm1"]/ancestor::label[contains (@class, "invalid")]/following-sibling::span',
        'confirm_2': '//input[@id="confirm2"]/ancestor::label[contains (@class, "invalid")]/following-sibling::span'
    }
