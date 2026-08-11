import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 314) - 155
    _mask = _data(75, None)
    _enc = 195
    return _mask, _enc

def run():
    matrix = 'nDbPat+1xSD`.:>.mm~X$ 6_t5*{So'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
