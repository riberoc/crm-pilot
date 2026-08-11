import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 608) - 209
    _mask = _data(668, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = '=N8YZ$QwsF_c{{&@h&jas70 @{?OYk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
