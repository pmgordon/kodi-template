"""Tests for the Kodi Adapter"""

# pylint: disable=redefined-outer-name
# pylint: disable=unused-import
# pylint: disable=no-self-use
# pylint: disable=protected-access
# pylint: disable=too-few-public-methods

import pytest

from source.kodi_adapter import adapter
from source.kodi_adapter import kodi_list

from source.scraper import scraper

class TestKodiAdapter():
    """Test the kodi adapter"""

    def test_get_kodi_object_with_list(self, mocker):
        """Test the get kodi object fn"""
        patch_path = 'source.scraper.scraper.ScraperClient.process_main_request'
        mock_process_main_request = mocker.patch(patch_path)
        adapter.get_kodi_object("action=listing&category=Animals", "/some/path")
        assert mock_process_main_request.called_with({"action": "listing", "category": "Animals"},
                                                     "/some/path")

class TestEncodedUrl():
    """Tests for getting an encoded url"""
    def test_get_encoded_url(self):
        """Test getting encoded url"""
        expected_url = "action=listing&category=Animals"
        encoded_url = kodi_list.get_encoded_url(action="listing", category="Animals")
        assert encoded_url == expected_url

class TestValidatePlayable():
    """Test Validating Playable"""

    def test_validate_playable(self):
        """Test is playable"""
        playable = kodi_list._validate_is_playable("true")
        assert playable == "true"

    def test_validate_not_playable(self):
        """Test is not playable"""
        playable = kodi_list._validate_is_playable("false")
        assert playable == "false"

    def test_validate_invalid_selection(self):
        """Test is not playable"""
        with pytest.raises(ValueError) as message:
            kodi_list._validate_is_playable(True)
        assert str(message.value) == "Invalid Value for is playable, must the 'true' or 'false'"

class TestKodiObjects():
    """Tests the objects that get passed to main"""
    def test_kodi_list_item_info(self):
        """Test the kodi list_item info object"""
        list_item_info = kodi_list.KodiListItemInfo(title="yes")
        isinstance(list_item_info, kodi_list.KodiListItemInfo)

    def test_kodi_list_info_with_invalid_prop(self):
        """Test the kodi list_item art object"""
        with pytest.raises(ValueError) as message:
            kodi_list.KodiListItemInfo(bad_prop="some value")

        assert str(message.value) == "bad_prop not a valid value for KodiListInfo"

    def test_kodi_list_art(self):
        """Test the kodi list_item art object"""
        list_item_info = kodi_list.KodiListItemArt(thumb="/path/to/art.png")
        isinstance(list_item_info, kodi_list.KodiListItemArt)

    def test_kodi_list_art_with_invalid_prop(self):
        """Test the kodi list_item art object"""
        with pytest.raises(ValueError) as message:
            kodi_list.KodiListItemArt(bad_prop="/path/to/art.png")

        assert str(message.value) == "bad_prop not a valid value for KodiListArt"

    def test_kodi_listitem(self):
        """Test the kodi list_item art object"""
        art = kodi_list.KodiListItemArt(thumb="/path/to/art.png")
        info = kodi_list.KodiListItemInfo(title="yes")
        url = kodi_list.get_encoded_url(action='listing', category="Animals")
        list_item = kodi_list.KodiListItem(url, "false", info=info, art=art)
        isinstance(list_item, kodi_list.KodiListItem)

    def test_kodi_object_with_list(self):
        """Test the kodi list_item art object"""

        #Setup
        art = kodi_list.KodiListItemArt(thumb="/path/to/art.png")
        info = kodi_list.KodiListItemInfo(title="yes")
        url = kodi_list.get_encoded_url(action='listing', category="Animals")
        list_item = kodi_list.KodiListItem(url, "false", info=info, art=art)
        videos = [list_item]

        #Test
        kodi_object = kodi_list.KodiObject("list", videos)

        #Verify
        isinstance(kodi_object, kodi_list.KodiObject)

    def test_kodi_object_with_invalid_list(self):
        """Test the kodi list_item art object"""

        #Setup
        videos = ["just-some-string"]

        #Verify
        with pytest.raises(ValueError) as message:
            kodi_list.KodiObject("list", videos)

        assert str(message.value) == ("KodiObject parm obj must be a"
                                      " list of KodiListItems when type is list")

    def test_kodi_object_with_list_type_but_not_a_list(self):
        """Test the kodi list_item art object"""

        #Setup
        videos = "just-some-string"

        #Verify
        with pytest.raises(ValueError) as message:
            kodi_list.KodiObject("list", videos)

        assert str(message.value) == ("KodiObject parm obj must be a"
                                      " list of KodiListItems when type is list")

    def test_kodi_object_with_video(self):
        """Test the kodi list_item art object"""
        #Setup
        url = "/path/to/video"

        #Test
        kodi_object = kodi_list.KodiObject("video", url)

        #Verify
        isinstance(kodi_object, kodi_list.KodiObject)

    def test_kodi_object_with_invalid_video(self):
        """Test the kodi list_item art object"""
        #Setup
        url = ["/path/to/video"]

        #Verify
        with pytest.raises(ValueError) as message:
            kodi_list.KodiObject("video", url)

        assert str(message.value) == ("KodiObject parm obj must be a str "
                                      "(video url) when type is video")

    def test_kodi_test_with_invalid_object(self):
        """Test when non-video or list is sent"""

        #Setup
        art = kodi_list.KodiListItemArt(thumb="/path/to/art.png")
        info = kodi_list.KodiListItemInfo(title="yes")
        url = kodi_list.get_encoded_url(action='listing', category="Animals")
        list_item = kodi_list.KodiListItem(url, "false", info=info, art=art)
        videos = [list_item]

        #Test / Verify
        with pytest.raises(ValueError) as message:
            kodi_list.KodiObject("something_else", videos)

        assert str(message.value) == "KodiObject attr type must be a video or list"
