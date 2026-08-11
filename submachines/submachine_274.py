import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 265) - 473
    _mask = _data(780, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'C}OaHc`Q86 ^{_8t/%A]wET6[O[tT%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
