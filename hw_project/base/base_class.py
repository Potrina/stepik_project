import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    # method get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    # method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('good value url')

    # method screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        self.driver.save_screenshot(f'./screen/screenshot{now_date}.png')
