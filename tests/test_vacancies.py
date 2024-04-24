from data.data_company import Data
from pages.search_page import SearchPage

def test_search_company():
    search_page = SearchPage()

    data = Data(
        main = 'Yellow - молодая компания, которая занимается разработкой мобильных приложений, облачных систем, а также систем с использованием AI и машинного обучения',
        goal = 'Наш главный ориентир',
        relationship = 'Такого же отношения',
        values='Наши ценности',
        achievements = 'Наши достижения',
        offer = 'компания предлагает соискателям'
    )

    search_page.open()
    search_page.search()
    search_page.should_have_company(data)
