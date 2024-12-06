import os
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class RegistrationTestClass(BaseCase):
    # baseUrl = "http://sbhfl.dev.intoto.nu/sbhfl-balie"
    # baseUrl = "https://staging.sbhfl.nl/sbhfl-balie"
    baseUrl = "https://sbhfl.nl/sbhfl-balie"


    def test_aanmelding_afgeronde_studie(self):
        self.open(self.baseUrl + "/aanmelden-afgeronde-studie/")
        self.click('input[name="reg[reg_geslacht]"]')
        self.type('input[name="reg[reg_voornaam]"]', "test_user")
        self.type('input[name="reg[reg_initialen]"]', "abc")
        self.type('input[name="reg[reg_achternaam]"]', "test_user")
        self.type('input[name="reg[reg_gebdatum]"]', "12345678")
        self.type('input[name="reg[reg_gebplaats]"]', "plaats")
        self.type('input[name="reg[reg_adres]"]', "adres")
        self.type('input[name="reg[reg_postcode]"]', "1234ab")
        self.type('input[name="reg[reg_plaats]"]', "plaats")
        self.type('input[name="reg[reg_telnummer]"]', "06123456789")

        email = self.generate_random_email()
        self.type('input[name="reg[reg_email]"]', email)
        self.type('input[name="emailConfirm"]', email)


        self.select_option_by_value('select[name="reg[reg_zh_id]"]', '85')
        self.check_if_unchecked('input[name="ignore_radio_opleiding"][value="nee"]')
        self.check_if_unchecked('#radio_gehaald_nee')
        self.check_if_unchecked('#vooropleiding_HAVO')
        self.type('input[name="reg[reg_diplomajaar]"]', "2020")

        # Upload test file
        dir_name = os.path.dirname('/Users/roygroothulze/Downloads')
        my_file = "AAAA-Test.pdf"
        file_path = os.path.join(dir_name, "Downloads/%s" % my_file)
        self.choose_file('input[name="upload"]', file_path)

        self.check_if_unchecked('#conditions')

        self.click('button[type="submit"]')

        self.wait(seconds=15)


    def generate_random_email(self):
        import random
        import string
        domains = ["example.com", "test.com", "sample.org", "test.nl", "example.nl"]
        letters = string.ascii_lowercase
        email = 'intoto-' + ''.join(random.choice(letters) for i in range(10)) + "@" + random.choice(domains)
        return email