#(7) 문자열 내림차순으로 배치하기

def solution(s):
    return ''.join(sorted(list(s),reverse=True))
	