import MapReduce
import sys

"""
DNA Sequence Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    seq_id = record[0]
    nucleotide = record[1]
    trimmed = nucleotide[:-10]
    mr.emit_intermediate(trimmed, seq_id)

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
