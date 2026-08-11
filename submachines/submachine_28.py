import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 309) - 386
    _mask = _data(150, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'W~iAUkxP$ =V?C`0yyd]g&[-<@7-ZE'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
