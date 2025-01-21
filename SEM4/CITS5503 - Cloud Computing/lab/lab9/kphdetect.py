import boto3

#Test provided in Lab Sheet
test = ["The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
        "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.",
        "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir",
        "L'amor che move il sole e l'altre stelle."]

for sentence in test:
    client = boto3.client('comprehend')
    response_lng = client.detect_dominant_language(Text=sentence)
    lng_code = response_lng['Languages'][0]['LanguageCode']
    response_kpd = client.detect_key_phrases(Text=sentence, LanguageCode=lng_code)
    keyPhrases = response_kpd['KeyPhrases']
    print(f"In the sentence:\n\"{sentence}\"\n")
    print("Detection")
    print("---------")
    for kp in keyPhrases:
        print(f"Keyphrase: {kp['Text']} | Confidence: {int(kp['Score']*100)}%")
    print("\n")

    