
def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Hola"):
        return "Hola muy buenas este BOT fue diseñado por Paulo Moreno\n para más información escribe ayuda"

    if user_message in ("ayuda"):
        return "los siguientes comandos que ofrecemos son:\npresion : resolvemos todas tus dudas respecto a como está tu presión arterial\nvacuna: aqui esclarecemos tus dudas sobre la vacuna , consultamos a medicos profesionales así que ninguno de estos datos están manipulados y son 100%\ntiempo(Ciudad): aqui preguntas sobre la previsión del tiempo de tu respectiva ciudad\nloteria aqui te informamos de las loterias más importantes de España\nfutbol te informaremos sobre el calendario de partidos de esta semana y daremos en tiempo real la información de como va el partido del respectivo equipo\ncuando: te damos las fechas de los eventos más importantes de España"
    
    if user_message in ("presion"):

        return "Como sé que mi presión está alta?\nCuando es mayor 130/80 mm Hg.\n\nComo sé que mi presión está baja?\nCuando es inferior a 60 mm Hg.\n\nCuál es una presión normal?\nLa presión arterial normal para adultos se define como una presión sistólica de menos de 120 y una presión diastólica de menos de 80."
    
    if user_message in ("vacuna"):

        return "Cuando me toca vacunarme?\nSegún la pagina Generalitat Valenciana (Cuando sea su turno de vacunación, de acuerdo con la estrategia de vacunación establecida por el Ministerio de Sanidad, el sistema valenciano de salud contactará con usted para citarle.)en otras palabras , te llamarán cuando te toque.\n\n por que me duele el brazo con la vacuna?\n El dolor se debe en parte a la reacción inflamatoria que se produce tras inocular la vacuna: Tu cuerpo recibe eso como una agresión y empieza a reaccionar para empezar esa respuesta inmune y, más adelante, crear los anticuerpos contra esa enfermedad,\n\nComo conseguir el pasaporte covid?\n atraves de la página https://coronavirus.san.gva.es/es/certificado-digital-ue y le daras un toque donde está escrito: solicitar certificado covid digital UE"

    if user_message in ("loteria"):

        return "Que dias juega bonolotto?\nLos sorteos tienen lugar los lunes, martes, miércoles, jueves, viernes y sábado a las 21:30 horas.\n\nQue dias juega la primitiva?\nEl sorteo se produce cada jueves y cada sábado a las 21:40 h\n\nCuando es la loteria Nacional?\n\nSemanalmente y de forma ordinaria se celebran sorteos los jueves y sábados. Los sorteos especiales sustituyen al ordinario de sábados y se celebran ese mismo día. Los sorteos extraordinarios se celebran en fechas determinadas."


  