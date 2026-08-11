import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 557) - 908
    _mask = _data(387, None)
    _enc = 32
    return _mask, _enc

def run():
    matrix = 'n} 0H%|;Lh[q4V`yQ?J&fzJhaw/0;B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
