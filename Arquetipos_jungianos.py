def cuestionario_arquetipos():
    print("Cuestionario para determinar tu arquetipo jungiano")
    print("Por favor, responde a las siguientes preguntas en una escala de 1 a 5, donde 1 es 'No en absoluto' y 5 es 'Totalmente de acuerdo'.")

    respuestas = []

    preguntas = {
        "Naturaleza": "Siento una fuerte conexión con la naturaleza.",
        "Creatividad": "Me considero una persona creativa y artística.",
        "Responsabilidad": "Tengo un fuerte sentido de la responsabilidad y el deber.",
        "Introspección": "Soy introspectivo y tiendo a reflexionar sobre mis pensamientos y emociones.",
        "Aprendizaje": "Tengo una gran sed de conocimiento y aprendizaje.",
        "Ayuda": "Me gusta ayudar a los demás y cuidar de su bienestar.",
        "Aventura": "Me atrae la aventura y la exploración.",
        "Sociabilidad": "Soy una persona muy sociable y me gusta estar rodeado de amigos.",
        "Rebeldía": "Me considero una persona rebelde y poco convencional.",
        "Estructura": "Tengo una fuerte necesidad de estructura y orden en mi vida.",
        "Ambición": "Soy ambicioso y me esfuerzo por alcanzar mis metas.",
        "Pasión": "Soy una persona enérgica y apasionada.",
        "Compromiso social": "Me preocupo profundamente por los problemas sociales y políticos.",
        "Soñador": "Soy un soñador y tiendo a vivir en mi mundo de fantasía.",
        "Misterio": "Me siento atraído por lo misterioso y lo desconocido.",
        "Liderazgo": "Soy un líder natural y me gusta tomar el control de las situaciones.",
        "Emocionalidad": "Soy una persona muy emocional y sensible.",
        "Valores tradicionales": "Me identifico con los valores tradicionales y conservadores.",
        "Pensamiento lógico": "Soy un pensador lógico y analítico.",
        "Independencia": "Tengo una fuerte necesidad de libertad e independencia.",
        "Inocente": "Tienes un espíritu puro e ingenuo, y a menudo ves el mundo con ojos de asombro.",
        "Creador": "Eres una persona creativa y artística que tiende a dar vida a nuevas ideas y proyectos.",
        "Héroe": "Tienes un fuerte sentido del deber y a veces asumes roles de liderazgo en situaciones difíciles.",
        "Sabio": "Eres una persona sabia y reflexiva, con una profunda comprensión de la vida y la mente humana.",
        "Explorador": "Te sientes atraído por la aventura y la exploración de lo desconocido.",
        "Rebelde": "Eres un espíritu rebelde que desafía las normas y convenciones establecidas.",
        "Amante": "Valoras las relaciones y la intimidad, y te entregas apasionadamente a tus seres queridos.",
        "Cuidador": "Tienes una fuerte inclinación a cuidar y proteger a los demás, y te preocupas por su bienestar.",
        "Constructor": "Eres un constructor y organizador, a menudo creas estructuras y sistemas sólidos.",
        "Director": "Eres un líder que guía y dirige a otros hacia metas comunes.",
        "Soñador": "Eres un soñador creativo que a menudo vive en un mundo de fantasía e imaginación.",
        "Jugador": "Disfrutas de la diversión y la emoción de la vida, y a menudo te tomas la vida como un juego.",
        "Creador de cambios": "Eres un agente de cambio que trabaja para transformar la sociedad y el mundo.",
        "Mago": "Tienes un profundo conocimiento y habilidades mágicas para transformar la realidad.",
        "Mártir": "Estás dispuesto a sacrificarte por los demás y a soportar el sufrimiento en nombre de tus creencias.",
        "Seductora": "Tienes un encanto y una seducción irresistibles que atraen a los demás hacia ti.",
        "Heraldo": "Eres un mensajero y portador de noticias, a menudo revelando verdades importantes.",
        "Trickster": "Eres un bromista y un agitador que cuestiona la autoridad y las normas establecidas.",
        "Mentor": "Tienes la sabiduría y la experiencia para guiar y enseñar a otros en su camino.",
        "Innovador": "Eres un innovador y un visionario que genera ideas revolucionarias y soluciones creativas.",
        "Guardián": "Tienes una fuerte inclinación a proteger y cuidar, a menudo asumiendo un papel de guardian en la vida de los demás.",
        "Constructor de sueños": "Tienes la capacidad de convertir sueños en realidad y crear un mundo mejor.",
        "Estratega": "Eres un estratega y planificador hábil, capaz de abordar desafíos de manera metódica y efectiva.",
        "Perfeccionista": "Buscas la perfección en todo lo que haces y te esfuerzas por lograr la excelencia.",
        "Científico": "Tienes una mente analítica y científica, siempre buscando comprender el mundo de manera objetiva.",
        "Artista": "Expresas tu creatividad a través del arte y la belleza en todas sus formas.",
        "Pensador libre": "Eres un pensador libre y un espíritu independiente que valora la autenticidad y la libertad.",
        "Pacificador": "Tienes la habilidad de mediar y traer paz a situaciones conflictivas.",
        "Escéptico": "Cuestionas las creencias y las afirmaciones, y buscas la verdad a través de la duda y la investigación.",
        "Romántico": "Eres un romántico que valora la pasión y la conexión emocional en las relaciones.",
        "Realista": "Eres pragmático y realista, abordando la vida con un enfoque lógico y práctico.",
        "Sanador": "Tienes la capacidad de sanar a otros y de traer alivio a través de tu compasión y cuidado.",
        "Explorador del espacio": "Sueñas con explorar el cosmos y buscas explorar lo desconocido en el espacio.",
        # Continuar agregando más arquetipos y preguntas aquí.
    }

    reglas_arquetipos = {
        "Inocente": lambda respuestas: sum(respuestas[:10]) <= 30 and sum(respuestas[10:]) <= 30,
        "Creador": lambda respuestas: sum(respuestas[:10]) <= 30 and sum(respuestas[10:]) > 30,
        "Héroe": lambda respuestas: sum(respuestas[:10]) > 30 and sum(respuestas[10:]) <= 30,
        "Sabio": lambda respuestas: respuestas[3] >= 4 and respuestas[8] >= 4,
        "Explorador": lambda respuestas: respuestas[6] >= 4 and respuestas[12] >= 4,
        "Rebelde": lambda respuestas: respuestas[16] >= 4 and respuestas[17] >= 4,
        "Amante": lambda respuestas: respuestas[7] >= 4 and respuestas[13] >= 4,
        "Cuidador": lambda respuestas: respuestas[5] >= 4 and respuestas[9] >= 4,
        "Constructor": lambda respuestas: respuestas[4] >= 4 and respuestas[18] >= 4,
        "Director": lambda respuestas: respuestas[15] >= 4 and respuestas[19] >= 4,
        "Soñador": lambda respuestas: respuestas[11] >= 4 and respuestas[14] >= 4,
        "Jugador": lambda respuestas: respuestas[1] >= 4 and respuestas[2] >= 4,
        "Creador de cambios": lambda respuestas: respuestas[7] >= 4 and respuestas[16] >= 4,
        "Mago": lambda respuestas: respuestas[3] >= 4 and respuestas[19] >= 4,
        "Mártir": lambda respuestas: respuestas[2] >= 4 and respuestas[17] >= 4,
        "Seductora": lambda respuestas: respuestas[13] >= 4 and respuestas[18] >= 4,
        "Heraldo": lambda respuestas: respuestas[8] >= 4 and respuestas[15] >= 4,
        "Trickster": lambda respuestas: respuestas[16] >= 4 and respuestas[17] <= 2,
        "Mentor": lambda respuestas: respuestas[3] >= 4 and respuestas[19] <= 2,
        "Innovador": lambda respuestas: respuestas[11] >= 4 and respuestas[4] <= 2,
        "Guardián": lambda respuestas: respuestas[5] >= 4 and respuestas[9] <= 2,
        "Constructor de sueños": lambda respuestas: respuestas[4] >= 4 and respuestas[18] <= 2,
        "Estratega": lambda respuestas: respuestas[10] >= 4 and respuestas[14] <= 2,
        "Perfeccionista": lambda respuestas: respuestas[1] >= 4 and respuestas[12] <= 2,
        "Científico": lambda respuestas: respuestas[2] >= 4 and respuestas[17] <= 2,
        "Artista": lambda respuestas: respuestas[6] >= 4 and respuestas[13] <= 2,
        "Pensador libre": lambda respuestas: respuestas[11] >= 4 and respuestas[14] <= 2,
        "Pacificador": lambda respuestas: respuestas[5] >= 4 and respuestas[9] <= 2,
        "Escéptico": lambda respuestas: respuestas[8] >= 4 and respuestas[15] <= 2,
        "Romántico": lambda respuestas: respuestas[7] >= 4 and respuestas[12] <= 2,
        "Realista": lambda respuestas: respuestas[10] >= 4 and respuestas[19] <= 2,
        "Sanador": lambda respuestas: respuestas[3] >= 4 and respuestas[18] <= 2,
        "Explorador del espacio": lambda respuestas: respuestas[6] >= 4 and respuestas[16] <= 2,
        # Agregar más reglas aquí para otros arquetipos.
    }

    for categoria, pregunta in preguntas.items():
        respuesta = int(input(f"{pregunta} (1-5): ").strip())
        while respuesta < 1 or respuesta > 5:
            respuesta = int(input("Por favor, responde en una escala de 1 a 5: ").strip())
        respuestas.append(respuesta)

    arquetipos_resultado = []

    for arquetipo, regla in reglas_arquetipos.items():
        if regla(respuestas):
            arquetipos_resultado.append(arquetipo)

    if not arquetipos_resultado:
        print("\nNo se pudo determinar un arquetipo específico con las respuestas proporcionadas.")
    else:
        print("\nResultados:")
        print("-" * 20)
        print("Los arquetipos sugeridos son:")

        total_respuestas = len(arquetipos_resultado)

        for resultado in arquetipos_resultado:
            porcentaje = (arquetipos_resultado.count(resultado) / total_respuestas) * 100
            print(f"- {resultado}: {preguntas[resultado]} ({porcentaje:.2f}%)")

cuestionario_arquetipos()
