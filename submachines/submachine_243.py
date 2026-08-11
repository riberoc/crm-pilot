import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 878) - 344
    _mask = _data(368, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = '+Us8CZ@v-w0v^.XzsEK< 42+^WDfd$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
