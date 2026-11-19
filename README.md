# Afritech Sports website: build source

The live site (branch `main`) is generated from these files.

- `content.py`: all text in English, French and Kiswahili, the products, events and NEWS items (each with a date and pillar; it drops off New/News after 7 days)
- `build.py`: writes the site into `out/`; copy `out/` onto `main` to publish
- `img/`: web-sized photos used on the site
- `apps_script.gs`: the Google Apps Script that saves visitor answers to the private Sheet
- `qa.py`, `qa2.py`: phone-width layout and picker checks
