from selene import browser, have

class SearchPage:
    def open(self):
        browser.open('https://rabota.by/')
        return self

    def search(self):
        browser.element('[data-qa="search-input"]').type('Yellow').press_enter()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="employersList"]').click()
        browser.element('.item--M8c5L2cxia1xqTMmWUFN .bloko-link.bloko-link_disable-visited').click()

    def should_have_company(self, data):
        browser.element('[data-qa="company-description-text"] .g-user-content').all('p').should(have.texts(
            data.main,
            data.goal,
            data.relationship,
            data.values,
            data.achievements,
            data.offer
        ))
