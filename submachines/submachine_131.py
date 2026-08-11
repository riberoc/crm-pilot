import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 167) - 430
    _mask = _data(555, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'G p5s#E?5XD%jJT{h[/bgNGJ[*HBo}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
