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


async def getWeatherData():
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


# To run the async function
asyncio.run(getWeatherData())
asyncio.run(screenshots())
