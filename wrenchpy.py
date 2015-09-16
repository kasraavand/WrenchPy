class datastructure(object):

	"""this class is contain the functions that has beed writen for interact
	with data structural tasks.  
	"""

	def find_intersection(m_list):
		"""
			g=[[], [], [0, 2], [1, 5], [0, 2, 3, 7], [4, 6], [1, 4, 5, 6], [], [], [3, 7]]
			s=map(set,g)
			print find_intersection(s)
			[set([0, 2, 3, 7]), set([1, 4, 5, 6])]
		"""
	    for i,v in enumerate(m_list) : 
	        for j,k in enumerate(m_list[i+1:],i+1):
	           if v & k:
	              m_list[i]=v.union(m_list.pop(j))
	              return find_intersection(m_list)
	    return m_list
		
	def typecounter(iterable,tp):
		"""
		    typecounter([1,2,[[[]]],[[]],3,4,[1,2,3,4,[[]]] ],list)
		    8
		"""
		return sum(1+typecounter(i,tp) for i in iterable if isinstance(i,tp))

	def split_with_iterable(main_list,delimiters):
		"""
		    split an iterable like a list with another iterable
		
		"""
		from itertools import groupby
        return [list(g) for k, g in groupby(main_list, delimiters.__contains__) if not k]

class text(object):
	"""
		contains the functions for doing text processing tasks
	"""
