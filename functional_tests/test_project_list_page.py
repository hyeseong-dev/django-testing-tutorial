
import time
from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.headless = True
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument("--single-process")
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(executable_path='./functional_tests/chromedriver', chrome_options=self.chrome_options)
    
    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)