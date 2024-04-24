from selene import browser, have

from data.data_company import DataCompany, DataSearchWithFilter
from pages.search_page import SearchPage

def test_search_company():
    search_page = SearchPage()

    data = DataCompany(
        main = 'Yellow - молодая компания, которая занимается разработкой мобильных приложений, облачных систем, а также систем с использованием AI и машинного обучения',
        goal = 'Наш главный ориентир',
        relationship = 'Такого же отношения',
        values='Наши ценности',
        achievements = 'Наши достижения',
        offer = 'компания предлагает соискателям'
    )

    search_page.open()
    search_page.search_company()
    search_page.should_have_company(data)

def test_advanced_search():
    search_page = SearchPage()

    data = DataSearchWithFilter(
        python='Python'
    )

    search_page.open()
    search_page.search_with_filters(data)
    search_page.should_have_search_with_filters(data)
