import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 357) - 436
    _mask = _data(160, None)
    _enc = 1
    return _mask, _enc

def run():
    matrix = 'K}Inc]w=&b!*X9H<e%4luWj+.l/#{Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
