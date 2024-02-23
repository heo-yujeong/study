KEY = 1004

def encode_decode(num):
    return num ^ KEY

print(encode_decode(1000))
print(encode_decode(4))

t = 1
for i in range(5):
    print(bin(t), t)
    t = t << 1


M = 31
N = 5
def Test():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return False
        tar = tar >> 1
    return True
print(Test())