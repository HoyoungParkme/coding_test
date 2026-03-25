N = int(input()) # 몇 번 반복된 "IOI" 형태를 만들지
M = int(input()) # 문자열 S의 길이
S = input() # 검사할 문자열 S

# 숫자가 너무 커지는 걸 막기 위한 값 (나머지 연산에 사용)
mod = 1e9 + 7

# 31의 거듭제곱 값을 저장할 리스트
# 예: [1, 31, 31^2, 31^3, ...]
po = [0] * M

# 첫 값은 31^0 = 1
po[0] = 1

# 31의 거듭제곱들을 차례대로 계산
for i in range(1, M):
    po[i] = (po[i - 1] * 31) % mod


# 우리가 찾고 싶은 문자열을 만듦 (처음은 "I")
Pn = "I"
for i in range(N):
    Pn += "OI"

# 찾고 싶은 문자열의 길이
K = len(Pn)

# 우리가 찾고 싶은 문자열의 해시값 (숫자 형태)
Pn_hash = 0

# 문자열을 숫자로 바꿔서 하나의 큰 숫자로 만듦
for i in range(K):
    Pn_hash = (Pn_hash * 31 + (ord(Pn[i]) - ord('A') + 1)) % mod

# S의 처음 K글자 해시값 (처음 비교할 구간)
S_hash = 0

# S의 앞에서부터 K글자를 이용해 해시값 계산
for i in range(K):
    S_hash = (S_hash * 31 + (ord(S[i]) - ord('A') + 1)) % mod

# 찾고 싶은 문자열이 몇 번 나오는지 셀 변수
count = 0

# S에서 길이 K짜리 문자열을 하나씩 확인
for i in range(M - K + 1):

    # 해시값이 같으면 같은 문자열일 가능성이 큼
    if S_hash == Pn_hash:
        count += 1

    # 다음 칸으로 이동할 수 있을 때만 실행
    if i + K < M:

        # 현재 구간에서 맨 앞 글자를 숫자로 바꿈
        # 이 글자는 다음 구간에서 빠짐
        first_char = ord(S[i]) - ord('A') + 1

        # 맨 앞 글자가 해시에서 차지하던 값을 빼줌
        S_hash = (S_hash - first_char * po[K - 1]) % mod

        # 한 칸 왼쪽으로 밀기 (자릿수 이동)
        S_hash = (S_hash * 31) % mod

        # 다음 구간에서 새로 들어오는 글자를 뒤에 추가
        S_hash = (S_hash + (ord(S[i + K]) - ord('A') + 1)) % mod

# 최종 결과 출력
print(count)