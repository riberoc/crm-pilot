import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 525) - 739
    _mask = _data(273, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = 'r^{aDH9j6M? o+qZTtu0qrfpFy!3u>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
