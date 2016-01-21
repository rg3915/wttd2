def cpf_checksum(cpf):
    """
    CPF Checksum algorithm.
    """
    if cpf in map(lambda x: str(x) * 11, range(0, 10)):
        return False

    def dv(partial):
        s = sum(b * int(v)
                for b, v in zip(range(len(partial) + 1, 1, -1), partial))
        return s % 11

    dv1 = 11 - dv(cpf[:9])
    q2 = dv(cpf[:10])
    dv2 = 11 - q2 if q2 >= 2 else 0

    return dv1 == int(cpf[9]) and dv2 == int(cpf[10])


def tests():
    assert cpf_checksum('11144477735') == True
    assert cpf_checksum('21111111120') == True
    assert cpf_checksum('00000000000') == False

tests()
