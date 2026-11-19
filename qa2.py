import asyncio,urllib.parse
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={"width":375,"height":800})
    await pg.add_init_script("window.open=function(u){window.__u=u}")
    await pg.goto("http://localhost:8765/technology/?lang=fr&src=li")
    await pg.click("#insait-joy [data-pick]")
    await pg.select_option("#pk-type","club");await pg.select_option("#pk-team","women");await pg.select_option("#pk-level","top")
    await pg.fill("#pk-country","Uganda");await pg.fill("#pk-city","Kampala");await pg.check("#pk-ok")
    await pg.screenshot(path="q-pick2.png")
    await pg.click("[data-p=go_wa]");print(urllib.parse.unquote(await pg.evaluate("window.__u")))
    await b.close()
asyncio.run(main())
