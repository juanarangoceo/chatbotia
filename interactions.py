import openai
import config

def handle_interaction(message, session):
    step = session["step"]
    
    if step == 0:
        if "cafetera" in message.lower():
            session["step"] = 1
            return "¡Hola! ☕ Soy *Juan*, tu asesor de café. Te ayudaré a encontrar la mejor opción. *¿Desde qué ciudad nos escribes?* 🏙️"

    elif step == 1:
        session["data"]["city"] = message
        session["step"] = 2
        return f"📍 Confirmado, enviamos a *{message}* con pago contra entrega 🚛. *¿Deseas conocer nuestros precios?*"

    elif step == 2 and "sí" in message.lower():
        session["step"] = 3
        return "💲 *Precio Especial CYBER DAYS* 🚚\n1️⃣ Máquina Automática para Café\n💵 *$420,000* Pago al recibir.\n*¿Qué uso le darás a la máquina?*"

    elif step == 3:
        session["data"]["uso"] = message
        session["step"] = 4
        return "✅ Perfecto, nuestra máquina te facilitará esa tarea. *¿Deseas que te enviemos el producto y lo pagas al recibir?*"

    elif step == 4 and "sí" in message.lower():
        session["step"] = 5
        return "📝 Para confirmar, por favor envía los siguientes datos:\n1️⃣ *Nombre*\n2️⃣ *Apellido*\n3️⃣ *Teléfono*\n4️⃣ *Departamento*\n5️⃣ *Ciudad*\n6️⃣ *Dirección*\n7️⃣ *Color*"

    elif step == 5:
        session["step"] = 6
        session["data"]["pedido"] = message
        return "✅ Confirmado. ¿Todos los datos son correctos?"

    elif step == 6 and "sí" in message.lower():
        return "🎉 ¡Pedido confirmado! En breve recibirás la confirmación de envío. 🚛"

    return "🤖 No entendí bien, ¿puedes repetirlo?"
