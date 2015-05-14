import MapReduce
import sys

"""
Relational join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #key: order_id
    #value: entire record
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):

    lineItemTable = []
    orderTable = []

    for value in list_of_values:
        if value[0] == "line_item":
            lineItemTable.append(value)
        else:
            orderTable.append(value)

    for order in orderTable:
        for item in lineItemTable:
            mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
