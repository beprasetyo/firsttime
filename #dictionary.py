#dictionary

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'Indonesia':'Jakarta',
            'Russia':'Moscow',
            'Germany':'Berlin'}

capitals.update({'China':'Beijing'})
capitals.update({'Indonesia':'IKN'})
#print(capitals['Germany'])
#print(capitals.get('Thailand'))
#print(capitals.keys())
#print(capitals.values())
print(capitals.items())

#for key,value in capitals.items():
#    print(key,value)