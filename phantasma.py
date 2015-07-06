class datastructure(object):

	"""this class contains functions for interaction between datastructural tasks
	   like lists,tuples,dictionaries and ... 
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
		