N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

print(round(sum([X[i] * W[i] for i in range(len(X))])/sum(W),1))