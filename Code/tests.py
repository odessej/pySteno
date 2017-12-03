"""
Testing for the module.

Includes all the test for the different image format
"""
import unittest
import os
import filecmp
from collections import deque
import steno

result_dir = 'results'
key_file = os.path.join(result_dir, 'key.txt')
text_file = os.path.join(result_dir, 'test.txt')
audio_file = os.path.join(result_dir, 'test.mp3')

res_text_file = os.path.join(result_dir, 'test2.txt')
res_audio_file = os.path.join(result_dir, 'test2.mp3')

exp_text_file = os.path.join(result_dir, 'res_expected.txt')
exp_audio_file = os.path.join(result_dir, 'res_expected.mp3')


def join_filename(file, ext):
    """Return path to file."""
    return os.path.join('image_test', file + ext)


class TestHiddingRetreving(unittest.TestCase):
    """Testing class for the hide and retrive functions."""

    def test_bmp(self):
        """Testing .bmp format."""
        ext = '.bmp'
        # With .txt data
        steno.hide_file_in_photo(text_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_text_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_text_file, exp_text_file))
        # Remove files
        os.remove(res_text_file)
        os.remove(join_filename('test2', ext))

        # With .mp3 data
        steno.hide_file_in_photo(audio_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_audio_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_audio_file, exp_audio_file))
        # Remove files
        os.remove(res_audio_file)
        os.remove(join_filename('test2', ext))

    def test_png(self):
        """Testing .png format."""
        ext = '.png'
        # With .txt data
        steno.hide_file_in_photo(text_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_text_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_text_file, exp_text_file))
        # Remove files
        os.remove(res_text_file)
        os.remove(join_filename('test2', ext))

        # With .mp3 data
        steno.hide_file_in_photo(audio_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_audio_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_audio_file, exp_audio_file))
        # Remove files
        os.remove(res_audio_file)
        os.remove(join_filename('test2', ext))

    def test_tiff(self):
        """Testing .tiff format."""
        ext = '.tiff'
        # With .txt data
        steno.hide_file_in_photo(text_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_text_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_text_file, exp_text_file))
        # Remove files
        os.remove(res_text_file)
        os.remove(join_filename('test2', ext))

        # With .mp3 data
        steno.hide_file_in_photo(audio_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_audio_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_audio_file, exp_audio_file))
        # Remove files
        os.remove(res_audio_file)
        os.remove(join_filename('test2', ext))

    def test_tif(self):
        """Testing .tif format."""
        ext = '.tif'
        # With .txt data
        steno.hide_file_in_photo(text_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_text_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_text_file, exp_text_file))
        # Remove files
        os.remove(res_text_file)
        os.remove(join_filename('test2', ext))

        # With .mp3 data
        steno.hide_file_in_photo(audio_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_audio_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_audio_file, exp_audio_file))
        # Remove files
        os.remove(res_audio_file)
        os.remove(join_filename('test2', ext))

    def test_tga(self):
        """Testing .tga format."""
        ext = '.tga'
        # With .txt data
        steno.hide_file_in_photo(text_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_text_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_text_file, exp_text_file))
        # Remove files
        os.remove(res_text_file)
        os.remove(join_filename('test2', ext))

        # With .mp3 data
        steno.hide_file_in_photo(audio_file, join_filename('test', ext),
                                 join_filename('test2', ext), True)
        steno.retrieve_file_in_photo(join_filename('test2', ext), res_audio_file)
        # Test if output is ok
        self.assertTrue(filecmp.cmp(res_audio_file, exp_audio_file))
        # Remove files
        os.remove(res_audio_file)
        os.remove(join_filename('test2', ext))


class TestFunction(unittest.TestCase):
    """Tests for functions."""

    def test_bit_and(self):
        """Test the function bit_and()."""
        # Setup
        lt_val = [0 for _ in range(0, 8)]
        val = '10101010'
        data = deque()
        data.append((int(val, 2), 7))

        for i in range(0, 4):
            val = val[2:]
            if not val:
                val = '0'

            result = steno.bit_and(lt_val[i], data)
            self.assertEqual(1, result)
            self.assertEqual(int(val, 2), data[0][0])

            result = steno.bit_and(lt_val[i + 1], data)
            self.assertEqual(0, result)
            self.assertEqual(int(val, 2), data[0][0])


def add_test_THR(suite_recv):
    """Adding test for the THR class."""
    suite.addTest(TestHiddingRetreving('test_bmp'))
    suite.addTest(TestHiddingRetreving('test_png'))
    suite.addTest(TestHiddingRetreving('test_tiff'))
    suite.addTest(TestHiddingRetreving('test_tif'))
    suite.addTest(TestHiddingRetreving('test_tga'))


def add_test_functions(suite_recv):
    """Adding the tests for the functions."""
    suite.addTest(TestFunction('test_bit_and'))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    add_test_functions(suite)
    add_test_THR(suite)  # Can be long. Took on my machine 165.378s
    runner.run(suite)
