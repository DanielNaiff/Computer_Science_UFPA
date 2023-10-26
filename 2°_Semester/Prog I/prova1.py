def quantos_cairam(coordenadas_fazenda, coordenadas_meteoritos):
    quantidade = 0
    for meteorito in coordenadas_meteoritos:
        if (meteorito[0] <= coordenadas_fazenda[0][0]) and (meteorito[1] <= coordenadas_fazenda[1][1]):
            quantidade += 1
    return quantidade

coordenadas_fazenda = [(3,1) , (1,5)]
coordenadas_meteoritos = [(3,2),(3,3),(2,3),(2,4),(3,5),(5,5),(1,1),(1,2),(1,3),(1,4)]

print(quantos_cairam(coordenadas_fazenda, coordenadas_meteoritos))


def quais_formam_linha_horizontal(coordenadas_meteoritos):
    meteoritos_horizontais = []
    for meteorito in coordenadas_meteoritos:
        for i in range(1, len(coordenadas_meteoritos)-1):
            if (meteorito[0] == coordenadas_meteoritos[i][0]) and ((meteorito[1] + 1) == coordenadas_meteoritos[i][1]):
                meteoritos_horizontais.append(meteorito)
                meteoritos_horizontais.append(coordenadas_meteoritos[i])
    return meteoritos_horizontais

print(quais_formam_linha_horizontal(coordenadas_meteoritos))

def gerador_mapa(coordenadas_meteoritos):
    mapa = {
            "Latitude": [],
            "Longitude": []
           }
    for meteorito in coordenadas_meteoritos:
       mapa["Latitude"].append(meteorito[0])
       mapa["Longitude"].append(meteorito[1])
    return mapa

print(gerador_mapa(coordenadas_meteoritos))
