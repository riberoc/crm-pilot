import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 236) - 958
    _mask = _data(1264, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = '->? (M!4-R$!w!IuL?>tbgpKr6%J5M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
