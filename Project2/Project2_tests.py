import unittest

from Project2 import *
# Write two test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        p1 = Point(5, 4)
        p2 = Point(10, 8)
        expected = Rectangle(Point(5, 8), Point(10, 4))
        result = create_rectangle(p1, p2)
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        p1 = Point(2, 2)
        p2 = Point(10, 10)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        result = create_rectangle(p1, p2)
        self.assertEqual(expected, result)

    def test_create_rectangle_3(self):
        p1 = Point(10, 10)
        p2 = Point(2, 2)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        result = create_rectangle(p1, p2)
        self.assertEqual(expected, result)

    def test_create_rectangle_4(self):
        p1 = Point(10, 2)
        p2 = Point(2, 10)
        expected = Rectangle(Point(2, 10), Point(10, 2))
        result = create_rectangle(p1, p2)
        self.assertEqual(expected, result)


    # Part 2

    def test_shorter_duration(self):
        d1 = Duration(10,20)
        d2 = Duration(5,17)
        expected = False
        result = shorter_duration_than(d1,d2)
        self.assertEqual(expected,result)

    def test_ShorterDurationThan_True(self):
        d1 = Duration(2, 30)
        d2 = Duration(3, 0)
        result = shorter_duration_than(d1, d2)
        expected = True
        self.assertEqual(expected, result)

    def test_ShorterDurationThan_False(self):
        d1 = Duration(4, 10)
        d2 = Duration(4, 5)
        result = shorter_duration_than(d1, d2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration_than_4(self):
        d1 = Duration(0, 90)  # 90 seconds total
        d2 = Duration(1, 20)  # 80 seconds total
        result = shorter_duration_than(d1, d2)
        self.assertEqual(False,result)


    # Part 3

    def test_songs_shorter_than(self):
        list1 = [Song("Bruh",'Bro',Duration(2,34)),Song("Yeahh",'Lessgo',Duration(1,32)),Song("67",'67',Duration(6,7)),Song("yeaa",'mann',Duration(0,120))]
        d1 = Duration(2,30)
        expected = [Song("Yeahh",'Lessgo',Duration(1,32)),Song("yeaa",'mann',Duration(0,120))]
        result = songs_shorter_than(list1,d1)
        self.assertEqual(expected,result)

    def test_SongShorterThan_Normal(self):
        s1 = Song("Song A", 'SongA',Duration(3, 30))
        s2 = Song("Song B",'SonB' ,Duration(4, 10))
        s3 = Song("Song C",'SongC', Duration(2, 45))

        upper = Duration(4, 0)

        result = songs_shorter_than([s1, s2, s3], upper)
        expected = [s1, s3]

        self.assertEqual(expected, result)
    # Part 4

    def test_running_time(self):
        s1 = Song("Song A", 'SongA', Duration(3, 30))
        s2 = Song("Song B", 'SonB', Duration(4, 10))
        s3 = Song("Song C", 'SongC', Duration(2, 45))

        playlist = [0,1,2]
        result = running_time([s1,s2,s3],playlist)
        expected = Duration(10,25)

        self.assertEqual(expected,result)

    def test_RunningTime_NormalPlaylist(self):
        s1 = Song("The Decemberists", "June Hymn", Duration(4, 30))
        s2 = Song("Broken Bells", "October", Duration(3, 40))
        s3 = Song("The Beatles", "Yellow Submarine", Duration(2, 45))
        songs = [s1, s2, s3]

        playlist = [0, 3]
        result = running_time(songs, playlist)
        expected = Duration(4, 30)

        self.assertEqual(expected, result)

    def test_RunningTime_SkipInvalidIndexes(self):
        s1 = Song("The Decemberists", "June Hymn", Duration(4, 30))
        s2 = Song("Broken Bells", "October", Duration(3, 40))
        songs = [s1, s2]

        playlist = [0, 5, 1, -2]
        result = running_time(songs, playlist)
        expected = Duration(8, 10)  # 4:30 + 3:40 = 8:10

        self.assertEqual(expected, result)

    # Part 5

    def test_validate_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['atascadero', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'creston']
        ]
        city_route = ['san luis obispo', 'santa margarita', 'atascadero']

        result = validate_route(city_links,city_route)
        expected = True
        self.assertEqual(expected,result)

    def test_validate_route2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['atascadero', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'creston']
        ]
        city_route = ['san luis obispo', 'atascadero']

        result = validate_route(city_links,city_route)
        expected = False
        self.assertEqual(expected,result)

    def test_validate_route_missing_middle_link(self):
        city_links = [
            ['a', 'b'],
            ['c', 'd'],
            ['d', 'e']
        ]

        route = ['a', 'b', 'c', 'd', 'e']

        result = validate_route(city_links, route)
        expected = False

        self.assertEqual(expected, result)

    def test_empty_route_is_valid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['atascadero', 'santa margarita'],
        ]
        route = []
        self.assertTrue(validate_route(city_links, route))

    def test_single_city_route_is_valid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['atascadero', 'santa margarita'],
        ]
        route = ['san luis obispo']
        self.assertTrue(validate_route(city_links, route))

    # Part 6

    def test_example_case(self):
        result = longest_repetition([1, 1, 2, 2, 1, 1, 1, 3])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        result = longest_repetition([])
        self.assertIsNone(result)

    def test_single_element(self):
        result = longest_repetition([5])
        self.assertEqual(result, 0)

    def test_tie_first_wins(self):
        result = longest_repetition([1, 1, 1, 2, 2, 2, 3])
        self.assertEqual(result, 0)

    def test_longer_sequence_in_middle(self):
        result = longest_repetition([7, 7, 5, 5, 5, 5, 9, 9])
        self.assertEqual(result, 2)

    def test_all_same_number(self):
        result = longest_repetition([4, 4, 4, 4, 4])
        self.assertEqual(result, 0)

    def test_no_repetitions(self):
        result = longest_repetition([1, 2, 3, 4, 5])
        self.assertEqual(result, 0)

    def test_repetition_at_end(self):
        result = longest_repetition([1, 2, 3, 3, 3, 3])
        self.assertEqual(result, 2)

    def test_repetition_at_beginning(self):
        result = longest_repetition([9, 9, 9, 9, 1, 2, 3])
        self.assertEqual(result, 0)

    def test_multiple_short_repetitions(self):
        result = longest_repetition([1, 1, 2, 2, 3, 3, 4, 4])
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        result = longest_repetition([100, 100, 100, 50, 50, 25])
        self.assertEqual(result, 0)

    def test_negative_numbers(self):
        result = longest_repetition([-1, -1, -1, -1, -1, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_broken_pattern(self):
        result = longest_repetition([5, 5, 5, 1, 5, 5, 5, 5])
        self.assertEqual(result, 4)

    def test_two_elements_same(self):
        result = longest_repetition([8, 8])
        self.assertEqual(result, 0)

    def test_two_elements_different(self):
        result = longest_repetition([3, 7])
        self.assertEqual(result, 0)

    def test_alternating_pattern(self):
        result = longest_repetition([1, 2, 1, 2, 1, 2, 2, 2, 2])
        self.assertEqual(result, 5)

    def test_very_long_repetition(self):
        result = longest_repetition([1] * 100 + [2, 3])
        self.assertEqual(result, 0)

    def test_multiple_ones_scattered(self):
        result = longest_repetition([1, 2, 3, 4, 4, 4, 5, 6])
        self.assertEqual(result, 3)
    def test_random_ones(self):
        result = longest_repetition([1,2,3,3,3,2,1,2,4,2,4,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,7,7])
        self.assertEqual(result,18)

    def test_in_case(self):
        result = longest_repetition([3,3,7,7])
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()
