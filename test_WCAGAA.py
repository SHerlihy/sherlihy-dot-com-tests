from playwright.sync_api import Page, expect

def getNonTextElements(page:Page):
    selectors = [
      'img',
      'canvas',
      'audio',
      'video',
      'input[type="image"]',
      'object',
      'embed'
    ];

    return page.locator(
        ", ".join(selectors)
    ).all()

def test_allSvgAria(page:Page):
    page.goto("https://sherlihy.com")
    allSvg = page.locator('svg').all()

    for svg in allSvg:
        hasAria = svg.get_attribute('aria-label') or svg.get_attribute('aria-hidden')
        
        if hasAria == None:
            expect.soft(svg, "Missing aria attribute")

# tbd
def test_nonTextContentAltText(page:Page):
    page.goto("https://sherlihy.com")
    nonTextElements = getNonTextElements(page)
    print(nonTextElements)

    for el in nonTextElements:
        altText = el.get_attribute('alt')
        print("ahhhh")
        
        if altText == None:
            expect.soft(el, "Missing alt attribute")
