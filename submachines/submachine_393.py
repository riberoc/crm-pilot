import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 781) - 375
    _mask = _data(263, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = 'MB[4# Ng9+`9i3G4tiaf9j-m+S@SQz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
