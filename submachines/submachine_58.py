import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 994) - 657
    _mask = _data(239, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'qnKo)]w)A7]{1iI@,}nQ UdWH6C,#Y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
