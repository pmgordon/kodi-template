"""Tests for Scraper"""
# pylint: disable=no-self-use

from source.scraper.scraper import ScraperClient


class TestScraping():
    """Test for the scraper functions"""
    def test_scraper(self):
        """Tests getting a scraper client"""
        scraper_client = ScraperClient()
        assert isinstance(scraper_client, ScraperClient)

    def test_get_categories(self):
        """Tests getting a scraper client"""
        scraper_client = ScraperClient()
        categories = scraper_client.get_categories()

        assert len(categories) == 3

    def test_get_videos_for_category(self):
        """Tests getting a scraper client"""
        scraper_client = ScraperClient()
        videos = scraper_client.get_videos_for_category("Animals")

        assert len(videos) == 3
