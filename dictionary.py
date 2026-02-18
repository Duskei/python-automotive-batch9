capitals = {'USA': 'Washington DC',
            'India': 'Delhi',
            'Russia': 'Moscow',
            'Japan' : 'Tokyo'
            }

print(capitals['Russia'])
print(capitals.get('Germany')) #none
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany' : 'Berlin'})
print("after updating: ", capitals)
capitals.update({'USA': 'Las vegas'})
print("2nd update", capitals)
capitals.pop('Russia')
print("after pop operation ", capitals)
capitals.clear()

for key,value in capitals.items():
    print(key,value)