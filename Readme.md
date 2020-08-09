# Template Kodi Video Plugin Project
Speed up the process of building video plugins.

## Starting a New Project

- Clone this repo
  - Setup the python environment.
    - `make init`
    - `source .pyenv/bin/activate`
    - `make pipreq`
  - Setup the kodi plugin
    - `make kodi-init`
      - This makes a soft link to the kodi plugin directory
    - edit the `addon.xml` file with the name and version of the plugin
    - `make kodi-deploy`
      - This makes an inital zip file that can be installed in kodi, after this is complete changes can be made and the `make kodi-push` will update the local version in kodi without having to install a new .zip file

## Directory Structure
- source/kodi_adapter/
  - source/kodi_adapter/adapter.py (Imported in main.py)
  - source/kodi_adapter/kodi_list.py (Imported the scraper module to build virtual kodi directories)
- source/scraper
  - source/scraper/scraper.py (Imported by adapter.py) 
    - Must implement: process_main_request and return a kodi_list.KodiObject

## Testing
- Run all tests: `make test`
- Run coverage report: `make coverage`
- Run linting report: `make lint`