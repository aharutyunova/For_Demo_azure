import config
from Pages.enter_qwallity import EntryQwallity
from Pages.home import Home
from Pages.register import Register
from Pages.login import Login


def test_register_user_with_valid_data(test_driver, test_logger):

    # activate Chrome browser
    entry_obj = EntryQwallity(test_driver, test_logger)
    entry_obj.go_to_page(config.url)

    # enter to qwallity app
    entry_obj.enter_to_qwallity_app()

    # Navigate to Register page
    home_obj = Home(test_driver, test_logger)
    home_obj.find_and_click(home_obj.btn_register_home)

    # register user
    register_obj = Register(test_driver, test_logger)
    user_name, password = register_obj.register_user()
    assert register_obj.find_elem_ui(home_obj.btn_login_home), test_logger.error("Login element is not displayed.")
    test_logger.info("User is registered successfully.")

    # login with registereed data
    login_obj = Login(test_driver, test_logger)
    home_obj.find_and_click(home_obj.btn_login_home)
    login_obj.login(user_name, password)
    assert home_obj.find_elem_ui(home_obj.btn_logout_home), test_logger.error("Login elementr is not displayed")
    test_logger.info("User is logged in successfully.")
