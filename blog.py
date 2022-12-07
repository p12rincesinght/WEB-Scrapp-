import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://www.placement-officer.com/2022/11/ey-internships-for-2023-batch-graduates.html")
    # create a screenshot of the page and save it
    await page.screenshot({"path": "pythoaaerreggggrean43.png"})
    # close the browser
    
    topics = await page.querySelectorAll(".MsoNormal")
    for topic in topics:
        title = await topic.getProperty("textContent")
           # print the article titles
        print(await title.jsonValue())
         


    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")