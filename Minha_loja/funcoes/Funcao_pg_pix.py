import flet as ft
import qrcode
import io
import base64

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

def main(page: ft.Page):
    page.title = "QR Code PIX"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    chave_pix = "bf688789-e586-4123-88b3-9c2bdcf42d43"

    valor_input = ft.TextField(label="Digite o valor (R$)", width=200)
    qr_image = ft.Image(width=200, height=200)  # QR Code menor
    copia_cola = ft.Text(value="", selectable=True)  # Texto copiável

    def gerar_qr(e):
        try:
            valor = float(valor_input.value) if valor_input.value else None
        except ValueError:
            valor = None

        payload = gerar_payload_pix(chave_pix, nome="Danillo", cidade="Manaus", valor=valor)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,  # reduzido para deixar menor
            border=2,
        )
        qr.add_data(payload)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        qr_image.src_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        copia_cola.value = payload  # mostra o código copia e cola
        page.update()

    gerar_btn = ft.ElevatedButton("Gerar QR Code", on_click=gerar_qr)

    page.add(valor_input, gerar_btn, qr_image, copia_cola)

ft.app(target=main)