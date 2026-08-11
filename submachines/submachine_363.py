import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 530) - 281
    _mask = _data(969, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = 'CiCP#;/8 )#r_z>r?bBfw$(Q6Wc-uQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
