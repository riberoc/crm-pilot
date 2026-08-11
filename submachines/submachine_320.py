import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 975) - 647
    _mask = _data(138, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = 'Q=UrN~pP-rAo 0Vstq7Cat:9s=N8Q>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
