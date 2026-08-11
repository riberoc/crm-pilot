import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 305) - 783
    _mask = _data(684, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = '_p /&~tdX^I!2EIK7X+:eOL%DAb3a/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
