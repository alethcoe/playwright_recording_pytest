def test_css_class(page):
    page.goto("/")
    page.click("text=Class Attribute")
    page.click(".btn-primary")

def test_hidden_layers(page):
    page.goto("/")
    page.click("text=Hidden Layers")
    page.click(".btn-success")

def test_click(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")
    page.click("#badButton")

def test_text_input(page):
    page.goto("/")
    page.click("text=Text Input")
    page.fill("#newButtonName", "Test Name")
    page.click('#updatingButton')
    assert page.inner_text('#updatingButton') == "Test Name"

def test_hidding_button(page):
    page.goto("/")
    page.click("text=Scrollbars")
    page.click('#hidingButton')

def test_dynamic_table(page):
    page.goto("/")
    page.click("text=Dynamic Table")

    columns = page.inner_html("//span[text()='CPU']/..")
    columnvalue = getColumnNumber(columns)
    chromeCPUText = page.inner_text(f"//span[text()='Chrome']/../span[{columnvalue}]")
    comparisonText = page.inner_text(".bg-warning")
    assert comparisonText == f"Chrome CPU: {chromeCPUText}"

#helper for dynamic table
def getColumnNumber(columns):
    headings = columns.split(">")
    for i in range(len(headings)):
        if headings[i].startswith('CPU'):
            return (i+1)/2
    return -1

def test_verify_text(page):
    page.goto("/")
    page.click("text=Verify Text")
    assert page.inner_text("//span[normalize-space(.)='Welcome UserName!']") == "Welcome UserName!"


def test_visibility(page):
    page.goto("/")
    page.click("text=Visibility")
    page.click('#hideButton')
    assert not page.is_visible("#removedButton")
    assert not page.is_visible("#zeroWidthButton")
    assert page.is_visible("#overlappedButton")
    assert page.is_visible("#transparentButton")
    assert not page.is_visible("#invisibleButton")
    assert not page.is_visible("#notdisplayedButton")
    assert page.is_visible("#offscreenButton")


def test_login_fail(page):
    page.goto("/")
    page.click("text=Sample App")
    page.fill('//input[@placeholder="User Name"]', 'Tim')
    page.click('#login')
    assert page.inner_text('#loginstatus') == 'Invalid username/password'

def test_login_logout(page):
    #login
    page.goto("/")
    page.click("text=Sample App")
    page.fill('//input[@placeholder="User Name"]', 'Tim')
    page.fill('//input[@name="Password"]', "pwd")
    page.click('#login')
    assert page.inner_text('#loginstatus') == 'Welcome, Tim!'

    #Logout
    page.fill('//input[@name="Password"]', "")
    page.click('#login')
    assert page.inner_text('#loginstatus') == 'User logged out.'

def test_mouseover_clicktwice(page):
    page.goto("/")
    page.click("text=Mouse Over")
    page.click('text=Click me')
    page.click('text=Click me')
    assert page.inner_text('#clickCount') == '2'

def test_nonbreakingspace(page):
    page.goto("/")
    page.click("text=Non-Breaking Space")
    page.click("text=My Button")

#https://www.tutorialspoint.com/pytest/pytest_run_tests_in_parallel.htm

# def test_progressbar(page):
#     page.goto("/")
#     page.click("text=Progress Bar")
#     page.click('#startButton')
#     page.inner_text("#progressBar[aria-valuenow='75']")
#     page.click('#stopButton')
#     assert "Result: 0" in page.inner_text('#result')

# def test_load_delay(page):
#     page.goto("/")
#     page.click("text=Load Delay")
#     page.click(".btn-primary")

# def test_ajax_data(page):
#     page.goto("/")
#     page.click("text=Ajax Data")
#     page.click(".btn-primary")
#     assert page.inner_text('.bg-success') == "Data loaded with AJAX get request."

# def test_clientside_delay(page):
#     page.goto("/")
#     page.click("text=Client Side Delay")
#     page.click(".btn-primary")
#     assert page.inner_text('.bg-success') == "Data calculated on the client side."