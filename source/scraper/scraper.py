"""This is the scraper module"""

# pylint: disable=no-self-use

from kodi_adapter.kodi_list import KodiObject
from kodi_adapter.kodi_list import KodiListItem
from kodi_adapter.kodi_list import KodiListItemArt
from kodi_adapter.kodi_list import KodiListItemInfo
from kodi_adapter.kodi_list import get_encoded_url

VIDEOS = {'Animals': [{'name': 'Crab',
                       'thumb': ('http://www.vidsplay.com/wp-content/'
                                 'uploads/2017/04/crab-screenshot.jpg'),
                       'video': 'http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4',
                       'genre': 'Animals'},
                      {'name': 'Alligator',
                       'thumb': ('http://www.vidsplay.com/wp-content/'
                                 'uploads/2017/04/alligator-screenshot.jpg'),
                       'video': 'http://www.vidsplay.com/wp-content/uploads/2017/04/alligator.mp4',
                       'genre': 'Animals'},
                      {'name': 'Turtle',
                       'thumb': ('http://www.vidsplay.com/wp-content/'
                                 'uploads/2017/04/turtle-screenshot.jpg'),
                       'video': 'http://www.vidsplay.com/wp-content/uploads/2017/04/turtle.mp4',
                       'genre': 'Animals'}
                      ],
          'Cars': [{'name': 'Postal Truck',
                    'thumb': ('http://www.vidsplay.com/wp-content/'
                              'uploads/2017/05/us_postal-screenshot.jpg'),
                    'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/us_postal.mp4',
                    'genre': 'Cars'},
                   {'name': 'Traffic',
                    'thumb': ('http://www.vidsplay.com/wp-content/'
                              'uploads/2017/05/traffic1-screenshot.jpg'),
                    'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/traffic1.mp4',
                    'genre': 'Cars'},
                   {'name': 'Traffic Arrows',
                    'thumb': ('http://www.vidsplay.com/wp-content/uploads/'
                              '2017/05/traffic_arrows-screenshot.jpg'),
                    'video': ('http://www.vidsplay.com/wp-content/uploads/'
                              '2017/05/traffic_arrows.mp4'),
                    'genre': 'Cars'}
                  ],
          'Food': [{'name': 'Chicken',
                    'thumb': ('http://www.vidsplay.com/wp-content/'
                              'uploads/2017/05/bbq_chicken-screenshot.jpg'),
                    'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/bbqchicken.mp4',
                    'genre': 'Food'},
                   {'name': 'Hamburger',
                    'thumb': ('http://www.vidsplay.com/wp-content/uploads/'
                              '2017/05/hamburger-screenshot.jpg'),
                    'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/hamburger.mp4',
                    'genre': 'Food'},
                   {'name': 'Pizza',
                    'thumb': ('http://www.vidsplay.com/wp-content/uploads/'
                              '2017/05/pizza-screenshot.jpg'),
                    'video': 'http://www.vidsplay.com/wp-content/uploads/2017/05/pizza.mp4',
                    'genre': 'Food'}
                  ]}


class ScraperClient():
    """The is the scraper class"""
    def __init__(self):
        self.base_url = "https://example.com"
        self.seasons = None

    def process_main_request(self, parms, profile_path):
        """Process the Main Path"""
        # pylint: disable=unused-argument

        if "action" not in parms:
            categories = self.get_categories()
            kodi_obj = KodiObject("list", categories)
            return kodi_obj

        if parms['action'] == 'listing':
            videos = self.get_videos_for_category(parms['category'])
            kodi_obj = KodiObject("list", videos)
            return kodi_obj

        if parms['action'] == 'play':
            kodi_obj = KodiObject("video", parms['video'])
            return kodi_obj

        raise ValueError("Invalid param given in process_main_process")


    def get_categories(self):
        """Get list of categories"""
        ret_list = []
        for category in VIDEOS:
            art = KodiListItemArt()
            info = KodiListItemInfo(title=category)
            url = get_encoded_url(action='listing', category=category)
            list_item = KodiListItem(url, "false", info=info, art=art)
            ret_list.append(list_item)

        return ret_list

    def get_videos_for_category(self, category_name):
        """Get List of Vidoes for Category"""
        ret_list = []
        for video in VIDEOS[category_name]:
            art = KodiListItemArt(thumb=video["thumb"], icon=video["thumb"])
            info = KodiListItemInfo(title=video["name"])
            url = get_encoded_url(action='play', video=video["video"])
            list_item = KodiListItem(url, "true", info=info, art=art)
            ret_list.append(list_item)

        return ret_list
    