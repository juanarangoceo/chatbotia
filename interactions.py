import openai
import config

PROMPT = """
Eres Juan, un asesor experto en café y ventas. Tu especialidad es la Cafetera Espresso Pro, un equipo diseñado para hacer espresso perfecto en casa. 
Tu tarea es guiar al cliente en la compra, respondiendo de forma clara, breve y persuasiva. 
Tu tono debe ser amigable, profesional y dinámico.

Estructura la conversación en 5 pasos:
1️⃣ Saludo e identificación de la necesidad.
2️⃣ Presentación del producto y beneficios.
3️⃣ Respuesta a preguntas del cliente.
4️⃣ Manejo de objeciones.
5️⃣ Cierre con llamado a la acción.

📌 Características principales:
✅ Espresso de calidad profesional.
✅ Espumador de leche de acero inoxidable para capuchinos.
✅ Doble filtro para preparar dos tazas a la vez.
✅ Pantalla táctil inteligente para fácil control.
✅ Material de acero inoxidable y tanque de agua de 1.5L.
✅ Presión de extracción de 20 bares.
✅ Garantía: 30 días de satisfacción + 3 meses por funcionamiento.

Si el usuario menciona palabras clave como "cafetera", "espresso", "capuchino" o "hacer café en casa", activa la conversación automáticamente. 
Siempre finaliza con un llamado a la acción para motivar la compra.
"""

def handle_interaction(message, session):
    step = session["step"]
    message = message.strip().lower()

    if step == 0:
        if any(word in message for word in ["cafetera", "espresso", "capuchino", "hacer café en casa"]):
            session["step"] = 1
            return "¡Hola! ☕ Soy *Juan*, tu asesor de café. *¿Desde qué ciudad nos escribes?* 🏙️"

    elif step == 1:
        session["data"]["city"] = message
        session["step"] = 2
        return f"📍 Confirmado, enviamos a *{message}* con pago contra entrega 🚛. *¿Deseas conocer nuestros precios?*"

    elif step == 2 and any(word in message for word in ["sí", "ok", "claro", "quiero", "precios", "cuales son los precios"]):
        session["step"] = 3
        return """
💲 *Precio Especial CYBER DAYS* 🚚
✅ Máquina Automática para Café
✅ Espumador de leche de acero inoxidable
✅ Pantalla táctil inteligente
✅ Tanque de agua de 1.5L
💵 *$420,000* Pago al recibir.
*¿Qué uso le darás a la máquina?*
"""

    elif step == 3:
        session["data"]["uso"] = message
        session["step"] = 4
        return "✅ Perfecto, nuestra máquina te facilitará esa tarea. *¿Deseas que te enviemos el producto y lo pagas al recibir?*"

    elif step == 4 and any(word in message for word in ["sí", "quiero", "envíenla", "lo compro"]):
        session["step"] = 5
        return """
📝 Para confirmar, por favor envía los siguientes datos:
1️⃣ *Nombre*
2️⃣ *Apellido*
3️⃣ *Teléfono*
4️⃣ *Departamento*
5️⃣ *Ciudad*
6️⃣ *Dirección*
7️⃣ *Color*
"""

    elif step == 5:
        session["step"] = 6
        session["data"]["pedido"] = message
        return "✅ Confirmado. ¿Todos los datos son correctos?"

    elif step == 6 and any(word in message for word in ["sí", "correcto", "están bien"]):
        return "🎉 ¡Pedido confirmado! En breve recibirás la confirmación de envío. 🚛"

    return "🤖 No entendí bien, ¿puedes repetirlo?"
