import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 806) - 401
    _mask = _data(425, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = '- 9vWy.^qQI!#94Y=@f_ZIv6t<mqT6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
