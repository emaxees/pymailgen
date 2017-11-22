import MarkupPy

index=open("index.html",'w')

title = input("Ingrese titulo del template: ");

page = MarkupPy.page(mode="html")

page.init(title=title,bodyattrs={'style':'border:0; padding:0; margin:0;'})

tablap_width=input("Ingrese ancho de la tabla principal: ")

page.table(width=tablap_width, border="0", cellspacing="0", cellpadding="0", align="center")
page.tbody()

c=0;
while(True):
    c+=1
    page.tr()
    print("Fila numero ",c)
    height_row=input("Ingrese el alto de la fila: ")



    colums_row=input("Ingrese el numero de columnas de la fila: ")
    if int(colums_row) !=0:
        page.td(height=height_row,width=tablap_width,colspan="3")
        page.table(height=height_row,width=tablap_width, border="0", cellspacing="0", cellpadding="0", align="center")
        page.tbody()
        for i in range(0,int(colums_row)):
            print("Columna numero ",i+1)
            row_colums=input("Ingrese numero de filas de la columna: ")
            if int(row_colums) !=0:
                '''No Funciona por el momento'''
            elif (int(row_colums)==0 and c>=0):
                width_colum=input("Ingrese el ancho: ")
                color=input("Ingrese color de la columna (HEX): ")
                color="#"+color
                answered=input("La columna tiene imagen s/n?: ")
                if answered=="s":
                    path=input("Ingrese numero del archivo: ")
                    path="images/img_"+str(path)+".jpg"
                    page.td(height=height_row,width=width_colum,bgcolor=color)
                    page.img( height=height_row,width=width_colum, alt='Publicidad', src=path,style="border:none;display:block;outline:none" )

                else:
                    page.td(height=height_row,width=width_colum,bgcolor=color)

                page.td.close()
        page.tbody.close()
        page.table.close()
        page.td.close()
        page.tr.close()

    else:
        color=input("Ingrese color de la columna (HEX): ")
        color="#"+color
        answered=input("La columna tiene imagen s/n?: ")
        if answered=="s":
            path=input("Ingrese numero del archivo: ")
            path="images/img_"+str(path)+".jpg"
            page.td(height=height_row,width=tablap_width,bgcolor=color,colspan="3")
            page.img( height=height_row,width=width_colum, alt='Publicidad', src=path,style="border:none;display:block;outline:none" )
        else:
            page.td(height=height_row,width=tablap_width,bgcolor=color,colspan="3")


        page.td.close()
        page.tr.close()


    q=input("Desea salir del asistente? s/n: ")
    if q=="s":
        if c>=1:
            page.tbody.close()
            page.table.close()

        else:
            page.tbody.close()
            page.table.close()
        break


index.write(str(page))

index.close()

b=input()
