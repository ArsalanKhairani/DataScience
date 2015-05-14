import MapReduce
import sys

"""
Inverted Index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    allDocs = []
    for doc in list_of_values:
        if doc not in allDocs:
            allDocs.append(doc)

    mr.emit((key, allDocs))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
