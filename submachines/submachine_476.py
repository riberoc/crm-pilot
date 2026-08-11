import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 798) - 894
    _mask = _data(173, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '-b,5t@7 ^_k6~(I@Sw5~sz<a9p4-wa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
