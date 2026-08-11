import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 587) - 197
    _mask = _data(879, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'P2VKbW1Zw9Bpuu[@(j[P{&nC,c3~~ '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
