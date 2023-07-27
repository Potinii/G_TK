def grupo_similar(lista):
       lista_agrupada = []
       elementos = set()
       for item in lista:
               if item in elementos:
                        for grupo in lista_agrupada:
                                 if item in grupo:
                                       grupo.append(item)
                                       break
       else:
              elementos.add(item)
              lista_agrupada.append([item])
       return lista_agrupada

lista = [12, 25, 1, 1, 7, 25]
lista_salida = grupo_similar(lista)
print(lista_salida)
