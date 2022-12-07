import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://www.amazon.in/OnePlus-Nord-Lite-128GB-Storage/dp/B09WQYFLRX?ref_=Oct_d_otopr_d_1805560031&pd_rd_w=Xbisr&content-id=amzn1.sym.f5d0d3e7-fe8a-4766-96ee-1c39e69d20b3&pf_rd_p=f5d0d3e7-fe8a-4766-96ee-1c39e69d20b3&pf_rd_r=9KHBYTQF55T0RJ1N6CDD&pd_rd_wg=7AkZy&pd_rd_r=88777a68-b37a-4367-937c-736cd4c60e37&pd_rd_i=B09WQYFLRX")
    
    # create a screenshot of the page and save it
    await page.screenshot({"path": "1234pyt67787865467hon43.png"})
    # close the browser
    
    topics = await page.querySelectorAll(".a-price-whole")
    for topic in topics:
        title = await topic.getProperty("textContent")
           # print the article titles
        print(await title.jsonValue())
         


    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")