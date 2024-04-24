from data.data_company import DataCompany, DataSearchWithFilter
from pages.search_page import SearchPage

search_page = SearchPage()

def test_search_company():
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
    data = DataSearchWithFilter(
        python = 'Python'
    )

    search_page.open()
    search_page.search_with_filters(data)
    search_page.should_have_search_with_filters(data)

def test_open_resume_page():
    search_page.open()
    search_page.search_resume_page()

def test_save_search_without_registering():
    search_page.open()
    search_page.save_search_without_registering()
    search_page.should_have_text_registering()

def test_choose_city():
    search_page.open()
    search_page.change_city()
    search_page.should_be_city()
