import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 402) - 547
    _mask = _data(1018, None)
    _enc = 95
    return _mask, _enc

def run():
    matrix = '0M<=lQAD:MQoxvm_mWk}AA^*1_ k%x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
