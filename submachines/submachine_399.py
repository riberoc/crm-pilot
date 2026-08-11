import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 117) - 824
    _mask = _data(920, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = '4R$0/KgZ#II%}{kJh nE9ZDXG+P[aV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
