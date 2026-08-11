import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 380) - 206
    _mask = _data(8, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = 'oxm?P`lu0N(2kD6F6GJx= >odgl9@t'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
