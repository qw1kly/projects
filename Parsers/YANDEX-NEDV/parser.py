import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebParser:
    def __init__(self, url = "https://realty.yandex.ru/moskva/snyat/kvartira/posutochno/"):
        self.driver = webdriver.Chrome()
        self.url = url

    async def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        await self.recaptcha()

    async def recaptcha(self):
        print("Решите капчу вручную, затем нажмите Enter в консоли...")
        input()
        await asyncio.sleep(2)

    async def get_blocks(self):
        return self.driver.find_elements(
            By.CSS_SELECTOR,
            'li.OffersSerpItem.OffersSerpItem_view_desktop.OffersSerpItem_format_full.OffersSerp__list-item.OffersSerp__list-item_type_offer'
          )

    async def pars_current_block(self, block):
        phone = None
        title_element = block.find_element(
            By.CSS_SELECTOR,
            'span[aria-level="3"][role="heading"].Text__text_m--1fDTw.Text__text_weight_500--1WBBj.OffersSerpItemTitle__title--1XhVm.Box__clr_primary--2uNHa span'
        )

        apartment_info = title_element.text.strip()

        button_selectors = [
            'button.Button.Button_js_inited.Button_size_m.Button_theme_realty.Button_type_button.Button_view_yellow.ItemShowPhone',
            'button.Button.Button_js_inited.Button_size_m.Button_theme_realty.Button_type_button.Button_view_soft-blue.ItemShowPhone',
            'button[class*="Button"][class*="ItemShowPhone"]'
        ]

        phone_button = None
        for selector in button_selectors:
            try:
                phone_button = block.find_element(By.CSS_SELECTOR, selector)
                break
            except:
                continue

        if phone_button:
            phone_button.click()
            await asyncio.sleep(2)

            phone_selectors = [
                'div[data-test="PhoneModalContactsPhoneShown"]',
                '.PhoneModalContacts__phone--3lu3b',
                'div[class*="PhoneModalContacts__phone"]'
            ]


            try:
                phone = None
                for selector in phone_selectors:
                    try:
                        phone_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                        phone = phone_element.text.strip()
                        break
                    except:
                        continue
            except Exception as e:
                print(f"Ошибка при поиске телефона")

            address_element = self.driver.find_element(By.CSS_SELECTOR, '.PhoneModalOffer__address')
            address = address_element.text.strip()

            close_attempt = 'svg.Icon__size_24--2vw-r.PhoneModal__closeIcon'

            element = self.driver.find_element(By.CSS_SELECTOR, close_attempt)
            element.click()

        if phone:
            with open("parsed.data", "a", encoding="UTF-8") as f:
                f.write(f"{apartment_info}$$${phone}$$${address}\n")

    async def parser(self):
        page = 1
        while page != 10:
            if page != 1:
                url = self.url + f"?page={page}"
                self.driver.get(url)
                await asyncio.sleep(5)

            blocks = await self.get_blocks()

            for block in blocks:
                await self.pars_current_block(block=block)
            page+=1
        self.driver.quit()
        await self.excel()

    async def excel(self):
        with open("parsed.data", encoding="UTF-8") as f:
            m =  list(f.readlines())
            result = list(set(m))
            m = result.copy()

            from openpyxl import Workbook
            wb = Workbook()
            sheet = wb.active
            sheet.title = "Квартиры"
            sheet['A1'] = "Площадь"
            sheet['B1'] = "Номер"
            sheet['C1'] = "Адрес"
            sheet['D1'] = "Согласие"
            s = 2
            for i in range(len(m)):
                data_to_excel = m[i].split("$$$")
                sheet["A"+str(s)] = data_to_excel[0]
                sheet["B"+str(s)] = data_to_excel[1]
                sheet["C"+str(s)] = data_to_excel[2]
                s+=1
            wb.save('обзвон.xlsx')

if __name__ == "__main__":


    async def main():
        parser = WebParser()
        await parser.start()
        await parser.parser()


    asyncio.run(main())