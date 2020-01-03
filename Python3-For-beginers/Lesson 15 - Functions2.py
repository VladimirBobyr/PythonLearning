
def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


user1 = create_record('Vasia', '774-567-456', 'Hvezdova 14')
user2 = create_record('Petia', '777-447-477', 'Ukrainska 65/5')

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Award to: " + person.title() + ' medal: ' + medal)


give_award('Za Berlin', 'Vasia', 'Petya')
give_award('Za Moscow', 'John', 'Ashley', 'Dormie')