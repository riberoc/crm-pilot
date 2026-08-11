import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 770) - 938
    _mask = _data(1836, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = '!i|:sfHLQ-N+AMR:wEw#j/3}/M D<6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
