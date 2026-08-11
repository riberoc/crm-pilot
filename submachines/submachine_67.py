import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 243) - 499
    _mask = _data(548, None)
    _enc = 230
    return _mask, _enc

def run():
    matrix = '7N 8%_O=AQ{4rtmjYJjr^j6LFV=hB<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
