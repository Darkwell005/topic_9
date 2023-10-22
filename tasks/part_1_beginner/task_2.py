word: str = input()
let: str = input()

if let not in word:
    print(-1)

else:
    find_index = -1
    for i in range(len(word)):

        if word[i] == let:
            find_index = i
            break

    print(find_index)
