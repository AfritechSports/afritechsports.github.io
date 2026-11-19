import asyncio
from playwright.async_api import async_playwright
B="http://localhost:8765/"
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();errs=[]
    pg=await b.new_page(viewport={"width":375,"height":800})
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("popup",lambda pp:errs.append("POPUP "+pp.url))
    for path in ["","technology/","advisory/","innovation/","privacy/"]:
      for l in ["en","fr","sw"]:
        await pg.goto(B+path+"?lang="+l);await pg.wait_for_timeout(150)
        ow=await pg.evaluate("document.documentElement.scrollWidth")
        # visible text in other languages?
        bad=await pg.evaluate("""(l)=>[...document.querySelectorAll('.t')].filter(e=>e.offsetParent!==null&&!e.classList.contains('t-'+l)).length""",l)
        hidden=await pg.evaluate("""(l)=>[...document.querySelectorAll('.t-'+l)].filter(e=>e.offsetParent===null&&!e.closest('.modal')&&!e.closest('[hidden]')).length""",l)
        news=await pg.evaluate("document.querySelectorAll('.ni').length")
        print(path or "home",l,"w",ow,"wrongLang",bad,"hiddenOwn",hidden,"news",news)
    await pg.goto(B+"?lang=sw");await pg.screenshot(path="q-home-sw.png",full_page=True)
    await pg.goto(B+"technology/?lang=en");await pg.screenshot(path="q-tech.png",full_page=True)
    await pg.goto(B+"advisory/?lang=fr");await pg.screenshot(path="q-adv.png",full_page=True)
    # picker flow
    await pg.goto(B+"technology/?lang=en&src=li")
    await pg.click("#insait-joy [data-pick]")
    await pg.wait_for_timeout(200)
    await pg.screenshot(path="q-pick.png")
    await pg.click("[data-p=go_wa]");print("err shown:",await pg.inner_text(".err"))
    await pg.select_option("#pk-type","club");await pg.select_option("#pk-team","women");await pg.select_option("#pk-level","top")
    await pg.fill("#pk-country","Uganda");await pg.fill("#pk-city","Kampala");await pg.check("#pk-ok")
    await pg.screenshot(path="q-pick2.png")
    async with pg.expect_popup() as pi: await pg.click("[data-p=go_wa]")
    pp=await pi.value;import urllib.parse;print(urllib.parse.unquote(pp.url))
    print("errors",errs);await b.close()
asyncio.run(main())
