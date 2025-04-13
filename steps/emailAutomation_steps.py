import os
from pytest_bdd import scenarios, given, when, then
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

emailBody = 'hopefully this gets me an interview :)'

@given('the browser is launched and the user navigates to the Gmail login page')
def open_login_page(page):
    page.goto('https://accounts.google.com/signin/v2/identifier?service=mail')

@given('the user inputs valid credentials')
def login(page):
    page.get_by_role('textbox', name='Email or phone').click()
    page.get_by_role('textbox', name='Email or phone').fill(os.getenv('USERNAME'))
    page.get_by_role('button', name='Next').click()
    page.get_by_role('textbox', name='Enter your password').click()
    page.get_by_role('textbox', name='Enter your password').fill(os.getenv('PASSWORD'))
    page.get_by_role('button', name='Next').click()

@then('the user should be logged in successfully')
def inbox_loaded(page):
    expect(page.get_by_role('link', name='Gmail', exact=True)).to_be_visible()

@given('the user creates a new email to a contact')
def create_email(page):
    #I am sorry about those static 1 second waits but i could not figure out why Google was not interacting with my locators and if i tried to use a dynamic wait it did not work. In reality I would discuss with colleagues to find a better solution
    composeMailLocator = page.locator('iframe[src*="https://docs.google.com/picker"]')
    page.get_by_role('button', name='Compose').click()
    page.get_by_role('link', name='Select contacts').click()
    page.wait_for_timeout(1000)     
    composeMailLocator.content_frame.get_by_role('checkbox', name='Select All').check()
    page.wait_for_timeout(1000)
    composeMailLocator.content_frame.get_by_role('button', name='Insert 1 item').click()
    page.get_by_role('textbox', name='Message Body').fill(emailBody)

@when('the user adds an attachment')
def attach_file(page):
    page.locator('input[type="file"]').set_input_files(os.path.abspath('just_a_pdf.pdf'))

@then('the attachment should be visible in the message')
def attachment_visible(page):
    expect(page.get_by_role('link', name='just_a_pdf.pdf (18K)')).to_be_visible()

@when('the user sends the email')
def send_email(page):
    page.get_by_role('button', name='Send ‪(Ctrl-Enter)‬').click()

@then('the email containing the message user composed should be in Sent messages')
def sent_email_visible(page):
    page.get_by_role('link', name='Sent').click()
    page.get_by_text('To: me', exact=True).first.click()
    expect(page.get_by_role('listitem')).to_contain_text(emailBody)

@when ('the user signs out')
def logout(page):
    page.locator('a[href*="https://accounts.google.com/SignOutOptions"]').click()
    page.locator('iframe[name=\'account\']').content_frame.get_by_role('link', name='Sign out').click()
    page.wait_for_url('https://workspace.google.com/intl/en-US/gmail/')

@then('the user should be redirected to the login page')
def logged_out(page):
    expect(page).to_have_url('https://workspace.google.com/intl/en-US/gmail/')