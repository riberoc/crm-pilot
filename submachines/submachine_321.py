import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 228) - 479
    _mask = _data(564, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = '4w/WIV@Vn(4.Y4s<NfK]d@4#1qG!1N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
