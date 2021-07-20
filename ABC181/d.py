from collections import Counter
from copy import copy

S = input()
ans = "No"

if len(S) == 1:
    if int(S) % 8 == 0:
        ans = "Yes"
elif len(S) == 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        ans = "Yes"
else:
    S_counter = Counter(S)
    for n in range(0, 1001, 8):
        counter = copy(S_counter)
        for c in str(n).zfill(3)[-3:]:
            if counter[c] > 0:
                counter[c] -= 1
            else:
                break
        else:
            ans = "Yes"

print(ans)
