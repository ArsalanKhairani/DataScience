import MapReduce
import sys

"""
Matrix Multiplication Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix_a_rows = 5
    matrix_b_cols = 5
    
    matrix = record[0]
    row = record[1]
    col = record[2]
    value = record[3]

    if matrix == "a":
        for k in range(matrix_b_cols):
            mr.emit_intermediate((row, k), (col, value))
    else:
        for i in range(matrix_a_rows):
            mr.emit_intermediate((i, col), (row, value))

def reducer(key, list_of_values):
    mul = {}
    for v in list_of_values:
        if v[0] not in mul.keys():
            mul[v[0]] = list()
            mul[v[0]].append(v[1])
        else:
            mul[v[0]].append(v[1])

    for v in mul:
        if len(mul[v]) > 1:
            temp = mul[v][0] * mul[v][1]
            mul[v] = temp
        else:
            mul[v] = 0

    mr.emit((key[0], key[1], sum(mul.values())))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
