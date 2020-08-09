"""Controller Adapter Between Kodi Main and the Scraper"""

# pylint: disable=broad-except

#import xbmc (Import if debugging)
#xbmc.log(parsed_parms, level=xbmc.LOGNOTICE)

try:
    from urllib.parse import parse_qsl
except Exception:
    from urlparse import parse_qsl

from scraper.scraper import ScraperClient

def get_kodi_object(params, profile_path):
    """
    Returns a directory list or video based on the specified path
    :param params: "argument=value" pairs
    :param profile_path: The full path to the profile dirctory
                         of the plugin, can be used to store a playlist for
                         the player, or saved results for faster app response
    :return: a list of files or a playable file
    """
    parsed_parms = dict(parse_qsl(params))

    scraper_client = ScraperClient()

    return scraper_client.process_main_request(parsed_parms, profile_path)
