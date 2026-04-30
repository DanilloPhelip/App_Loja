def crc16(payload: str) -> str:
    polinomio = 0x1021
    resultado = 0xFFFF
    for byte in payload.encode("utf-8"):
        resultado ^= (byte << 8)
        for _ in range(8):
            if (resultado & 0x8000):
                resultado = (resultado << 1) ^ polinomio
            else:
                resultado <<= 1
            resultado &= 0xFFFF
    return format(resultado, "04X")


def gerar_payload_pix(chave, nome="Danillo", cidade="Manaus", valor=None):
    payload = "000201"
    payload += "010212"

    gui = "BR.GOV.BCB.PIX"
    gui_field = f"00{len(gui):02}{gui}"
    chave_field = f"01{len(chave):02}{chave}"
    mai = gui_field + chave_field
    payload += f"26{len(mai):02}{mai}"

    payload += "52040000"
    payload += "5303986"

    if valor:
        valor_str = f"{valor:.2f}"
        payload += f"54{len(valor_str):02}{valor_str}"

    payload += "5802BR"
    payload += f"59{len(nome):02}{nome}"
    payload += f"60{len(cidade):02}{cidade}"

    ref = "***"
    add_data = f"05{len(ref):02}{ref}"
    payload += f"62{len(add_data):02}{add_data}"

    payload += "6304"
    crc = crc16(payload)
    payload += crc
    return payload
