def vista_habitantes(): 
    form = SQLFORM.grid(db.habitantes, paginate =20, csv=False,links=None, deletable=True, editable=True) 
   
    #csv es para no mostrar explortar,links: es de los botones de abajo , create: es de el boton añadir registro
    form2 = crud.create(db.habitantes)                                                   # form2 crea el formulario de arriba
    tipo = db(db.habitantes.cedula == request.vars.cedula).select()                      # hay tipo cuando la cedula=a una de la bd
    if form2.errors and tipo:                                                            #si hay error en form2 y hay tipo
        for x in tipo:
                 response.flash = "la cedula {0} ya existe,  pertenece a: {1} {2}".format(request.vars.cedula, x.nombres, x.apellidos)

    
    #form2.process()     #preguta: como recargar form cuando se inserta en form2?
    return dict(form = form, form2 = form2)#('current_record','reference habitantes',readable=False,writable=False)
