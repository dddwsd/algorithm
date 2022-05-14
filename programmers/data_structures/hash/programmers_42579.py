# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    dic = defaultdict(dict)
    for idx in range(len(genres)):
        genre = genres[idx]
        play = plays[idx]
        total[genre] += play
        dic[genre][idx] = play


    for genre, _ in sorted(total.items(), key = lambda x:x[1],reverse=True):
        songs = sorted(dic[genre].items(), key = lambda x: (-x[1], x[0]))
        for idx, (num, play) in enumerate(songs):
            if idx == 2:
                break
            answer.append(num)

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = [4,1,3,0]
if solution(genres,plays) == result:
    print('Success')
else:
    print('Fail')