xd = {
    'posilki': [
        {'nazwa': 'a', 'kalorie': 123, 'bialko': 123},
        {'nazwa': 'b', 'kalorie': 234, 'bialko': 234}],

    'treningi': [{'nazwa': '321', 'powtorzenia': 1, 'ciezar': 10}, {'nazwa': '532', 'powtorzenia': 3, 'ciezar': 5}]
}

bialko = 0

for i in range(len(xd['treningi'])):
    bialko += (xd['treningi'][i]['ciezar'] * xd['treningi'][i]['powtorzenia'])

print(bialko)