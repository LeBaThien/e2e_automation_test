from behave import given, when, then
from pages.HomePage import HomePage
from pages.SearchResultsPage import SearchResultsPage
from utils.helper import load_config

@given('I am on the Google home page')
def step_given_i_am_on_google_home_page(context):
    config = load_config()
    context.home_page = HomePage(context.driver)
    context.home_page.open(config['base_url'])

@when('I search for "{keyword}"')
def step_when_i_search_for_keyword(context, keyword):
    context.home_page.search(keyword)

@then("the results page is displayed")
def step_impl(context):
    search_results_page = SearchResultsPage(context.driver)
    assert search_results_page.is_results_page_displayed(), "Search results page is not displayed"
