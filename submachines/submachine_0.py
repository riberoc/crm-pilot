import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 125) - 880
    _mask = _data(1107, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'u08IQvg!o3.Mr|rH$J*^ G!><aDroP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
