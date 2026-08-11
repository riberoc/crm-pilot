import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 962) - 573
    _mask = _data(319, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'z4^N}_>]//)Y*<Xolg4 `bgE=vFB-}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
