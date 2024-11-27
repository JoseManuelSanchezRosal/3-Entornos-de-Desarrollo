'''Ejercicio 8: Envío de correos electrónicos. El siguiente código envía correos electrónicos. Refactorízalo para que las tareas 
de generar el asunto, el cuerpo del mensaje y el envío estén separadas.'''

# Código inicial
def enviar_correo(destinatario, asunto, mensaje):
    print(f"Enviando correo a: {destinatario}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
