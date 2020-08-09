"""Classes for Kodi Lists"""


# pylint: disable=too-few-public-methods
# pylint: disable=broad-except

try:
    from urllib.parse import urlencode
except Exception:
    from urllib import urlencode

class KodiListItemInfo():
    """
    List Item info valid arguments are listed as follows
    https://codedocs.xyz/AlwinEsch/kodi/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
    """
    def __init__(self, **kwargs):
        self.attributes = {}
        self._set_attributes(kwargs)

    def _set_attributes(self, kwargs):
        """Validate Set attributes"""
        valid_attributes = set(['count', 'size', 'date', 'genre',
                                'country', 'year', 'episode', 'season',
                                'sortepisode', 'sortseason', 'episodeguide',
                                'showlink', 'top250', 'setid', 'tracknumber',
                                'rating', 'userrating', 'watched', 'playcount',
                                'overlay', 'cast', 'castandrole', 'director',
                                'mpaa', 'plot', 'plotoutline', 'title',
                                'originaltitle', 'sorttitle', 'duration', 'studio',
                                'tagline', 'writer', 'tvshowtitle', 'premiered',
                                'status', 'set', 'setoverview', 'tag', 'imdbnumber',
                                'code', 'aired', 'credits', 'lastplayed', 'album',
                                'artist', 'votes', 'path', 'trailer', 'dateadded',
                                'mediatype', 'dbid'])

        for key, value in kwargs.items():
            if key not in valid_attributes:
                raise ValueError("{} not a valid value for KodiListInfo".format(key))
            self.attributes[key] = value


class KodiListItemArt():
    """Mimics the class of xbmcgui.ListItem Art Section"""
    def __init__(self, **kwargs):
        self.attributes = {}
        self._set_attributes(kwargs)

    def _set_attributes(self, kwargs):
        """Set Attributes for Kodi Art"""

        valid_attributes = set(['thumb', 'poster', 'banner',
                                'fanart', 'clearart', 'clearlogo',
                                'landscape', 'icon'])

        for key, value in kwargs.items():
            if key not in valid_attributes:
                raise ValueError("{} not a valid value for KodiListArt".format(key))
            self.attributes[key] = value

class KodiListItem():
    """Mimics the class of a xbmcgui.ListItem"""
    def __init__(self,
                 url,
                 is_playable,
                 info=KodiListItemInfo(),
                 art=KodiListItemArt()):

        self.info = info.attributes
        self.art = art.attributes
        self.url = url
        self.is_playable = _validate_is_playable(is_playable)

class KodiObject():
    """Object Class to return to main.py"""
    def __init__(self, object_type, obj):
        self.type = object_type
        self.obj = obj
        self._validate_object()

    def _validate_object(self):
        """Validate the input object"""
        if self.type == "video":
            if not isinstance(self.obj, str):
                raise ValueError(("KodiObject parm obj must be a "
                                  "str (video url) when type is video"))
            return

        if self.type == "list":
            self._validate_list_obj()
            return

        raise ValueError("KodiObject attr type must be a video or list")

    def _validate_list_obj(self):
        """Validate that the list of objects are list items"""
        if not isinstance(self.obj, list):
            raise ValueError(("KodiObject parm obj must be a "
                              "list of KodiListItems when type is list"))
        for obj in self.obj:
            if not isinstance(obj, KodiListItem):
                raise ValueError(("KodiObject parm obj must be a "
                                  "list of KodiListItems when type is list"))




def get_encoded_url(**kwargs):
    """Get a url encoded result"""
    return urlencode(kwargs)

def _validate_is_playable(is_playable):
    """Checks to see if is_playable is true or false"""

    if is_playable == "true":
        return is_playable

    if is_playable == "false":
        return is_playable

    raise ValueError("Invalid Value for is playable, must the 'true' or 'false'")
        