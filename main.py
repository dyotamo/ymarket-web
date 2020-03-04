from requests import get
from bs4 import BeautifulSoup
from model import Company, CurrentPage

companies = []
current_page = CurrentPage.get_or_create()[0]

try:
    while True:
        response = get(
            'https://www.gomarket.io/en/pagina/{}'.format(current_page.page))

        if response.status_code in [500, 404]:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        for div in soup.find_all('div', 'row-content'):
            try:
                company = Company()
                company.name = div.p.b.text
                company.category = div.find('span', 'category tag').text
                company.place = div.find_all('span', 'tag')[1].text
                company.address_phone = div.find(
                    'div', 'row-data contact-info homepage-contact-info').text
                company.image = div.find('img', 'company-logo')['src']
            except (IndexError, AttributeError, TypeError,):
                # Do nothing, just keep the field null
                pass

            company.save()
            companies.append(company)
            print(company)

        current_page.page += 1
        current_page.save()

    print('----------------------------------------------------')
    print('Scrapping closed with status: ', response.status_code)
except KeyboardInterrupt:
    pass
