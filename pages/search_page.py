from selene import browser, have, command, be

class SearchPage:
    def open(self):
        browser.open('https://rabota.by/')
        return self

    def search_company(self):
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

    def search_with_filters(self, data):
        browser.element('[data-qa="advanced-search"]').click()
        browser.element('[data-qa="vacancysearch__keywords-input"]').type(data.python)
        browser.element('[data-qa="bloko-suggest-list"] li:first-child').click()
        browser.element('[data-qa="resumesearch__profroles-switcher"]').click()
        browser.element('[data-qa="bloko-tree-selector-item-text bloko-tree-selector-item-text-category-11"]').click()
        browser.element('[data-qa="bloko-tree-selector-popup-submit"]').click()
        browser.element('[data-qa="advanced-search-salary"]').type('3000')
        browser.element('[data-qa="advanced-search-submit-button"]').click()

    def should_have_search_with_filters(self, data):
        browser.element('[data-qa="search-input"]').should(have.value(data.python))
        browser.element('[data-qa="bloko-header-3"]').should(have.text(data.python))

    def search_resume_page(self):
        browser.element('[data-qa="remote-item-desktop"]').perform(command.js.scroll_into_view).click()
        browser.element('[data-qa="bloko-modal-close"]').click()
        browser.element('[data-hh-tab-id="resumeSearch"]').click()
        browser.element('[data-qa="bloko-custom-select-select"]').click()
        browser.element('[data-qa="bloko-custom-select-option-list"]').should(be.visible)
