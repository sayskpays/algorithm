dic_data = {
    '2': ['A','B','C'],
    '3': ['D','E','F'],
    '4': ['G','H','I'],
    '5': ['J','K','L'],
    '6': ['M','N','O'],
    '7': ['P','Q','R','S'],
    '8': ['T','U','V'],
    '9': ['W','X','Y','Z']
}

dial = input()

for i in dial:
    for key, values in dic_data.items():
        print(values)
