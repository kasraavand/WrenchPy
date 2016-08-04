from collections import deque
from itertools import groupby
from math import sqrt


class datastructure(object):

    """This class is contain the functions that has been written for interacting
       with data structural tasks.
    """

    def find_intersection(self, m_list):
        """
            example:
            g=[[], [], [0, 2], [1, 5], [0, 2, 3, 7], [4, 6], [1, 4, 5, 6], [], [], [3, 7]]
            s=map(set,g)
            print find_intersection(s)
            [set([0, 2, 3, 7]), set([1, 4, 5, 6])]
        """
        for i, v in enumerate(m_list):
            for j, k in enumerate(m_list[i + 1:], i + 1):
                if v & k:
                    m_list[i] = v.union(m_list.pop(j))
                    return self.find_intersection(m_list)
        return m_list

    def typecounter(self, iterable, tp):
        """
            typecounter([1,2,[[[]]],[[]],3,4,[1,2,3,4,[[]]] ],list)
            8
        """
        return sum(1 + self.typecounter(i, tp) for i in iterable if isinstance(i, tp))

    def split_with_iterable(main_list, delimiters):
        """
            Split an iterable like a list with another iterable.

        """
        return [list(g) for k, g in groupby(main_list, delimiters.__contains__) if not k]


class text(object):
    """
        Contains functions related to text processing tasks.
    """

class Number(object):
    """Numberic tasks """
    def __init__(self):
        pass

    def find_min_square(self, n):
        """ Find the minimum number of square numbers in which a number can be partitioned to. """
        def check(num):
            sq = sqrt(num)
            int_sq = int(sq)
            return int_sq, sq

        def find2(num, int_sq):
            maps = deque()
            for i in range(int_sq, 0, -1):
                rem = num - i ** 2
                int_sq, sq = check(rem)
                if int_sq == sq:
                    return False
                maps.append(rem)
            return maps

        int_sq, sq = check(n)
        if int_sq == sq:
            return 1
        elif n == 2:
            return 2
        result = find2(n, int_sq)
        if not result:
            return 2
        else:
            for remind in result:
                int_sq, _ = check(remind)
                if remind == 2:
                    return 3
                result = find2(remind, int_sq)
                if not result:
                    return 3
        return 4
