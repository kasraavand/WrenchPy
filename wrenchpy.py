from collections import deque
from itertools import groupby
from functools import wraps
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

    def Find_largest_path(self, total, matrix):
        """
        Find most weighted path in a matrix (We only are allowed to move down and right)
        from top left cell to most bottom right cell which it's subtract from total is the minimum.
        If there is no path with a positive or zero reminder it returns -1.

        This function uses an optimized algorithm without recursive methods (for sake of memory
        optimization) and a cache decorator (for sake of time optimization and refuse of extra 
        calculations for same situations).
        """
        N = len(matrix) - 1
        remained_states = deque()
        y = x = path_sum = 0
        all_path = []
        blind_nodes = set()

        def cache_moves(f):
            cache = {}

            @wraps(f)
            def wrapped(*args):
                try:
                    result = cache[args]
                except KeyError:
                    result = cache[args] = f(*args)
                return result
            return wrapped

        def find_next_cells(y, x):
            if y == x == N:
                return False
            next_cells = {(y, min(x + 1, N)), (min(y + 1, N), x)}
            if (y, x) in next_cells:
                return next_cells.difference(((y, x),))
            else:
                return next_cells

        @cache_moves
        def move(y, x, path_sum):
            next_cells = find_next_cells(y, x)
            if not next_cells:
                # we are in last cell
                return False
            try:
                next_1, next_2 = next_cells
            except:
                new = next_cells.pop()
                if new in blind_nodes:
                    return None
            else:
                if next_1 in blind_nodes:
                    new = next_2
                elif next_2 in blind_nodes:
                    new = next_1
                else:
                    (n_1_y, n_1_x), (n_2_y, n_2_x) = next_1, next_2
                    if matrix[n_1_y][n_1_x] > matrix[n_2_y][n_2_x]:
                        new = next_1
                        remained_states.append((next_2, path_sum))
                    else:
                        new = next_2
                        remained_states.append((next_1, path_sum))
            finally:
                return new

        while True:
            if N == 0:
                return total
            next_cell = move(y, x, path_sum)
            try:
                new_y, new_x = next_cell
            except:
                if next_cell is False:
                    # we are in last cell
                    if not remained_states:
                        if all_path:
                            result = total - max(all_path)
                        else:
                            result = total - (path_sum + matrix[y][x])
                        if result < 0:
                            return -1
                        return result

                    else:
                        # backtrack
                        all_path.append(path_sum)
                        (new_y, new_x), path_sum = remained_states.pop()
                else:
                    # we are in blind node with one next
                    (new_y, new_x), path_sum = remained_states.pop()

            finally:
                value = matrix[new_y][new_x]
                if value > total:
                    blind_nodes.add((new_y, new_x))
                path_sum += value
                if new_y == new_x == N and path_sum == total:
                    return 0
                if path_sum >= total:
                    try:
                        (new_y, new_x), path_sum = remained_states.pop()
                    except:
                        if all_path:
                            return total - max(all_path)
                        return -1
                    else:
                        value = matrix[new_y][new_x]
                        path_sum += value
                y, x = new_y, new_x


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
