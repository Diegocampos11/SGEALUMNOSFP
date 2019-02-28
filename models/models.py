# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alumnosfp_empresa(models.Model):
    _name = 'alumnosfp.empresa'#nombre del modelo
    nombre = fields.Char( string = 'Nombre', required = True )
    direccion = fields.Char( string='Dirección' )
    #a una empresa pertenecen muchos alumnosfp
    alumnos = fields.One2many( 'alumnosfp.alumno', 'empresa', string='Lista de alumnos' )

class alumnosfp_alumno(models.Model):
    _name = 'alumnosfp.alumno'#nombre del modelo
    nombre = fields.Char( string = 'Nombre', required = True )#, help='Introduce el nombre'
    apellidos = fields.Char( string='Apellidos', required=True )
    fechaNacimiento = fields.Date( string='Fecha', required=True )
    cicloFormativo = fields.Selection( [ ( '0', 'DAM' ), ( '1', 'DAW' ), ( '2', 'ASIR' ) ] )
    nota = fields.Float( string='Nota', required=True )
    empresa = fields.Many2one( 'alumnosfp.empresa', string='Empresa', required=True, ondelete='cascade' )
    #campo generado
    notaMedia = fields.Char( string = 'Nota media', compute = '_notaMedia', store = True )
    @api.depends( 'nota' )
    #declaracion de un procedimiento
    #siempre lleva dos puntos al final de la declaración de una clase, procedimiento, while, for :o
    def _notaMedia( self ):
        for r in self:
            if r.nota >= 5 and r.nota < 7:
                r.notaMedia = 'Aprobado'
            elif r.nota >= 7 and r.nota < 9:
                r.notaMedia = 'Notable'
            elif r.nota >= 9 and r.nota <= 10:
                r.notaMedia = 'Sobresaliente'
