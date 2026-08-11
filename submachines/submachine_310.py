import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 247) - 783
    _mask = _data(896, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = '`:`(8iaC8! e0KBt]X#n+~A6ob~7]z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
