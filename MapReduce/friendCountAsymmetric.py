import MapReduce
import sys

"""
Friend Count (Asymmetric) Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    pA = record[0]
    pB = record[1]
    mr.emit_intermediate(pA, pB)
    mr.emit_intermediate(pB, pA)

def reducer(key, list_of_values):
    for friend in list_of_values:
        if not list_of_values.count(friend) > 1:
            mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
