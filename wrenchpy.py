from collections import deque
from itertools import groupby
from math import sqrt


class datastructure:

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

    def split_with_iterable(self, main_list, delimiters):
        """
            Split an iterable like a list with another iterable.

            >>> main_list = range(20)
            >>> delimiters = range(0, 20, 5)
            >>>
            >>> [list(g) for k, g in groupby(main_list, delimiters.__contains__) if not k]
            [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14], [16, 17, 18, 19]]
        """
        return [list(g) for k, g in groupby(main_list, delimiters.__contains__) if not k]

    def find_postorder(self, preorder, inorder, length, prestart=0, inostart=0):
        """
        Find the postorder traversal of a tree from it's preorder and inorder traversals.
        """
        if length == 0:
            yield

        for i in range(inostart, inostart + length):
            if preorder[prestart] == inorder[i]:
                break
        self.find_postorder(preorder, prestart + 1, inorder, inostart, i - inostart)
        self.find_postorder(preorder, prestart + i - inostart + 1, inorder, i + 1, length - i + inostart - 1)
        yield preorder[prestart]


class text:
    """
        Contains functions related to text processing tasks.
    """


class Number:
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
