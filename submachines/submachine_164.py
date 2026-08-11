import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 945) - 368
    _mask = _data(485, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = 'm{q51?!?BIfy|IA!^4eg<?e$bQ4v0L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
