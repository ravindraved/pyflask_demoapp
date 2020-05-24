
from lolviz import *
import refcycle
from print_schema import print_schema



stores = [

    {
        'name': 'store_1',
        'items':
            [
                {'name': 'store_1_item_1',
                 'price': 15.99,
                 'available_qty': 12},
                {
                    'name': 'store_1_item_2',
                    'price': 12.99
                }
            ]

    },

    {
        'name': 'store_2',
        'items': [
            {'name': 'store_2_item_1',
             'price': 15.99,
             'available_qty': 12
             },

            {'name': 'store_2_item_2',
             'price': 12.99,
             'available_qty': 12
             }
            ,

            {'name': 'store_2_item_3',
             'price': 12.99,
             'available_qty': 12
             }
        ]

    }

]

"""
g = listviz(stores)
print(g.source)
g.view()
"""


# note the Schema is printed based on the 1st element scan .. so if store items has additional attribute.. all those attributes has to be on the 1st stores..first item only!!
# say if i add new attribue to item in 2nd object of store.. or even 2nd item element of store 1 .. the schema will not pick that up.
# its not doing super set scan..its just 1st object scan..!
# this is good if the data structure is going to be consistent.. say from RDBMS.. but cannot be relied upon in case of noSql or flexible schema object graph!
# what u need in that case is another JSON Object schema validator .. or Schema Validation engine..!!... and debug it using the visual graphviz..refcyce library generated image!..or ofcourse.. Debugger of IDE!



print_schema(stores)


graph = refcycle.objects_reachable_from(stores)
graph
graph.export_image('example.svg')
