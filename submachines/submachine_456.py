import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 487) - 251
    _mask = _data(221, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'c7$k#xg!W2,n)c]gAL9#i<8 XuRElU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
