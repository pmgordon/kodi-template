"""Main process that gets called from XBMC"""

import sys
import xbmcgui
import xbmcplugin
import xbmcaddon

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

from kodi_adapter import adapter

def get_profile_path():
    """Create The playlist write Path"""
    addon = xbmcaddon.Addon()
    profile = xbmc.translatePath(addon.getAddonInfo('profile')).decode("utf-8")
    return profile

def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)

def process_object(kodi_object):
    if kodi_object.type == 'video':
        play_video(kodi_object.obj)
        return

    display_list(kodi_object.obj)

def display_list(list_object):
    xbmcplugin.setPluginCategory(_handle, "Hello")
    xbmcplugin.setContent(_handle, 'videos')

    for obj in list_object:

        list_item = xbmcgui.ListItem(label=obj.info['title'])
        list_item.setInfo('video', obj.info)
        list_item.setArt(obj.art)
        list_item.setProperty('IsPlayable', obj.is_playable)
        is_folder = False if obj.is_playable == 'true' else True
        url = '{0}?{1}'.format(_url, obj.url)

        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)

    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)

def router(parms):
    """This is the main router function"""
    kodi_object = adapter.get_kodi_object(parms, get_profile_path())
    process_object(kodi_object)


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
