from collections import defaultdict, deque
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]


def wordladder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    nei = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + '*' + word[j+1:]
            nei[pattern].append(word)

    visit = set([beginWord])
    q = deque([beginWord])
    # print(q)
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for neiword in nei[pattern]:
                    if neiword not in visit:
                        visit.add(neiword)
                        q.append(neiword)

        res += 1
    return res





print(wordladder(beginWord, endWord, wordList))