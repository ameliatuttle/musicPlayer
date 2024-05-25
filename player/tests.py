from unittest.mock import patch
from django.test import TestCase, override_settings
from django.urls import reverse
from django.conf import settings
import os

class SongLoadingTestCase(TestCase):
    @override_settings(STATICFILES_DIRS=[os.path.join(settings.BASE_DIR, 'static')])
    def setUp(self):
        # Create a mock static/music directory and add dummy MP3 files
        self.music_dir = os.path.join(settings.BASE_DIR, 'static/music')
        os.makedirs(self.music_dir, exist_ok=True)
        with open(os.path.join(self.music_dir, 'test_song_1.mp3'), 'wb') as f:
            f.write(b'This is a test song.')
        with open(os.path.join(self.music_dir, 'test_song_2.mp3'), 'wb') as f:
            f.write(b'This is another test song.')

    def tearDown(self):
        # Clean up the mock files after the test
        for file in os.listdir(self.music_dir):
            file_path = os.path.join(self.music_dir, file)
            os.remove(file_path)
        os.rmdir(self.music_dir)

    @patch('player.views.get_mp3_metadata')
    def test_songs_loading(self, mock_get_mp3_metadata):
        # Define the mock return value
        mock_get_mp3_metadata.return_value = {
            'title': 'Mock Title',
            'artist': 'Mock Artist',
            'album': 'Mock Album',
            'duration': 123,
            'release_year': '2020',
            'genre': 'Mock Genre'
        }

        response = self.client.get(reverse('index'))

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the response context contains the song details
        self.assertIn('title', response.context)
        self.assertIn('artist', response.context)
        self.assertIn('album', response.context)
        self.assertIn('duration', response.context)
        self.assertIn('file_name', response.context)

        # Check the context values
        self.assertEqual(response.context['title'], 'Mock Title')
        self.assertEqual(response.context['artist'], 'Mock Artist')
        self.assertEqual(response.context['album'], 'Mock Album')
        self.assertEqual(response.context['duration'], 123)

        # Check that the song file name is one of the test files
        self.assertIn(response.context['file_name'], ['test_song_1.mp3', 'test_song_2.mp3'])

