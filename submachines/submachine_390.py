import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 950) - 429
    _mask = _data(315, None)
    _enc = 232
    return _mask, _enc

def run():
    matrix = 'm~_|/I?e 6v3h2*#MY=ov{iwGbAiTd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
