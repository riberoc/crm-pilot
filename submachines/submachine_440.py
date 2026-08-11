import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 873) - 107
    _mask = _data(559, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = 'jdi3@kEW<0+k,B?@bKDS 2OAyUmiQ}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
