d = {

     "Key1" : 1,

     "Key2" : {

           "a" : 2,

           "b" : 3,

           "c" : {

                "d" : {

                       "y": 10

                     },

                "e" : 5

                }, 

                  }

}

# {

#   “key1”: 1,

#   “key2.a”: 2,

#   “key2.b”: 3,

#   “key2.c.d.y”: 10,

#   “key2.c.e”: 5

#   }


from collections import defaultdict, deque

# res = dict()
# def dfs(d):
#     global res
#     for key, value in d.items():
#         if not isinstance(value, dict):
#             res[key] = value
#         else:
#             dfs(value)

#     return res 


def solve(d):

    res = dict()
    queue = deque([d])
    
    while queue:
        node = queue.popleft()
        print(node)
        for key in node:
            temp = key
            if isinstance(node[key], dict):
                queue.append(node[key])
                
            else:
                res[key] = node[key]
    return res

print(solve(d))


