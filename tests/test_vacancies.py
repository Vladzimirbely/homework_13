from selene import browser, have

def test_search_login():
    browser.open('https://rabota.by/')
    browser.element('[data-qa="login"]').should(have.text('Войти'))

def test_type_text_input():
    browser.open('https://rabota.by/')
    browser.element('[data-qa="search-input"]').type('Python').press_enter()

def test_click_signup():
    browser.open('https://rabota.by/')
    browser.element('[data-qa="signup"]').click()
    browser.element('[data-qa="applicant-signup-title"]').should(have.text('Регистрация соискателя'))

def test_click_filter():
    browser.open('https://rabota.by/')
    browser.element('[data-qa="advanced-search"]').click()
    browser.element('[data-qa="bloko-header-1"]').should(have.text('Поиск вакансий'))

def test_click_search_employees():
    browser.open('https://rabota.by/')
    browser.element('.supernova-dashboard-link-switch').click()
    browser.element('[data-qa="employer-index-publish-vacancy"]').should(have.text('Разместить вакансию'))
