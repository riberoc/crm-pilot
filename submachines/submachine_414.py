import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 111) - 457
    _mask = _data(548, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = 'h;(lW=D6=v; ;{ZKKsy9`ZLKz|48eQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
