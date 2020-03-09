from sys import getsizeof

ID = 0
class Comission_v1:
    
    def __init__(self, name, reward, end_req):
        
        global ID
        self.ID = ID
        ID += 1
        
        self.name = name
        self.reward = reward
        self.end_req = end_req

comm_v1_1 = Comission_v1('name1', 'reward1', 'end_req1')
comm_v1_2 = Comission_v1('name2', 'reward2', 'end_req2')
comissions_v1 = [comm_v1_1, comm_v1_2]

comm_v2_1 = [1, 'name1', 'reward1', 'end_req1']
comm_v2_2 = [2, 'name2', 'reward2', 'end_req2']
comissions_v2 = [comm_v2_1, comm_v2_1]

comissions_v3 = [
                    {
                        'id': 1,
                        'name': 'name1',
                        'reward': 'reward1',
                        'end_req': 'end_req1'
                    },
                    {
                        'id': 2,
                        'name': 'name2',
                        'reward': 'reward2',
                        'end_req': 'end_req2'
                    }
                ]
out = getsizeof(comissions_v1) + getsizeof(Comission_v1)
for x in comissions_v1:
    out += getsizeof(x)
print(f'v1: class-{getsizeof(Comission_v1)}, all-{out}')

out = getsizeof(comissions_v2)
for x in comissions_v2:
    out += getsizeof(x)
print(f'v2: all-{out}')

out = getsizeof(comissions_v3)
for x in comissions_v3:
    out += getsizeof(x)
print(f'v3: all-{out}')
