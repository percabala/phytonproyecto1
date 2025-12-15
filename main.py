import os
from time import sleep
"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

# 1. Cambiar la variable de diccionario a 'dic_empresas'
dic_empresas = {
    # Usar RUC (11 dígitos) como clave, y 'razon_social'
    '20512345678':{
        'razon_social':'Tecnologias Peruanas SAC',
        'email' : 'contacto@tecperu.com'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    # Cambiar título
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESAS
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR
          """)
    print("=" * ANCHO)
    # Manejo de error de input
    try:
        opcion = int(input('INGRESE OPCIÓN : '))
    except ValueError:
        opcion = 0 # Opción inválida si no es un número
        
    os.system("clear")
    
    if opcion == 1:
        # CREATE: Registrar Empresa
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        # El identificador ahora es RUC
        ruc = input("Ingrese RUC: ")
        # El campo de nombre ahora es razon_social
        razon_social = input("Ingrese Razon Social: ")
        email = input("Ingrese Email: ")
        
        dic_nueva_empresa = {
            'razon_social': razon_social, # Usar nueva variable
            'email': email
        }
        dic_empresas[ruc] = dic_nueva_empresa # Usar nuevo diccionario y clave
        print("Empresa registrada existosamente")
        
    elif opcion == 2:
        # READ: Mostrar Empresas
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        # Iterar sobre el nuevo diccionario
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon Social : {info['razon_social']}") # Usar nueva clave
            print(f"Email : {info['email']}")
            print('*' * ANCHO)
            
    elif opcion == 3:
        # UPDATE: Actualizar Empresa
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC de la empresa a actualizar : ")
        
        if ruc in dic_empresas:
            # Usar nueva clave 'razon_social'
            print(f"Empresa Encontrada : {dic_empresas[ruc]['razon_social']}") 
            
            # Usar nueva clave 'razon_social'
            nueva_razon_social = input(f"NUEVA RAZON SOCIAL({dic_empresas[ruc]['razon_social']}) : ")
            nuevo_email = input(f"NUEVO EMAIL({dic_empresas[ruc]['email']}) : ")
            
            if nueva_razon_social:
                # Usar nueva clave 'razon_social'
                dic_empresas[ruc]['razon_social'] = nueva_razon_social
            if nuevo_email:
                dic_empresas[ruc]['email'] = nuevo_email
                
            print("EMPRESA ACTUALIZADA EXITOSAMENTE!!!")
        else:
            print('No se encontro la empresa para el RUC ingresado')
            
    elif opcion == 4:
        # DELETE: Eliminar Empresa
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        # El mensaje de input se corrigió de "actualizar" a "eliminar" para mayor claridad, aunque se mantiene el código original del input
        ruc = input("Ingrese RUC de la empresa a eliminar : ") 
        
        if ruc in dic_empresas:
            del dic_empresas[ruc] # Usar nuevo diccionario
            print('EMPRESA ELIMINADA EXITOSAMENTE')
        else:
            print('No se encontro la empresa para el RUC ingresado')
            
    elif opcion == 5:
        # SALIR
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(1)
        break
        
    else:
        print("OPCION NO VALIDA...")
        
    input("Presione ENTER para continuar...")