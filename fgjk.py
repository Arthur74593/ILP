N, K = map(int, input().split())
n = list(map(int, input().split()))
contador = 0
for indice in range(N):
  if n[indice] == K:
    contador += 1

