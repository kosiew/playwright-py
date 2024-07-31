import asyncio
import datetime

from playwright.async_api import async_playwright
from rich import print

url = "https://www.klmoneychanger.com/compare-rates?n=gbp"


async def get_browser_page(p):
    browser = await p.chromium.launch()
    context = await browser.new_context()
    page = await context.new_page()
    return browser, page


async def screenshots():
    async with async_playwright() as p:
        browser, page = await get_browser_page(p)

        await page.goto(url)
        await page.set_viewport_size({"width": 1920, "height": 1080})
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        await page.screenshot(path=f"mobile-{current_time}.png", full_page=True)

        await browser.close()


async def get_weather_data():
    async with async_playwright() as p:
        browser, page = await get_browser_page(p)

        await page.goto(
            "https://forecast.weather.gov/MapClick.php?lat=40.7533&lon=-73.9922"
        )

        temperature = await page.locator(".myforecast-current-lrg").all_inner_texts()
        humidity = await page.locator(
            "#current_conditions_detail > table > tbody > tr:nth-child(3) > td"
        ).all_inner_texts()

        print(temperature)
        print(humidity)

        await browser.close()


async def read_um_latest_headline():
    url = "https://um.edu.my/"
    locator = "xpath=/html/body/div[3]/div/div[2]/div/div[6]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[2]/h3"
    locator = ".gdlr-core-blog-grid .gdlr-core-blog-title.gdlr-core-skin-title"
    async with async_playwright() as p:
        browser, page = await get_browser_page(p)

        await page.goto(url)

        latest_headline = await page.locator(locator).all_inner_texts()

        print(latest_headline)

        await browser.close()


# To run the async function
asyncio.run(read_um_latest_headline())
