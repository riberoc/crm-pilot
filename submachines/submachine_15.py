import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 403) - 598
    _mask = _data(785, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '_N- $5fpB&@m?S$@35|xA!BG8!(3-@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
