# -*- coding: utf-8 -*-
{
    'name': "Alumnos FP",

    'summary': """
        Módulo para la gestión de alumnos de un centro FP""",

    'description': """
        Con este modulo puedes llevar el control de tus alumnos y podras almacenar información relativa a la empresa donde están realizando las practicas
    """,

    'author': "Diego SL",
    'website': "http://www.diegosl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        'security/security.xml',#PRIMERO EL XML
        #LUEGO EL access.csv, SIN ESPACIOS!!! :o y el atributo id hay que resptarlo como tal XD (supongo que es la entrada del registro o algo así xd)
        #el atributo model_id, siempre comenzara por model_NOMBRE_MODELO
        #name, nombre a mostrar de la entrada
        #group_id, id del grupo creado en security.xml
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_empresa.xml',#añadimos el nuevo fichero creado :D
        'data/data.xml'#añadimos datos precargados
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
