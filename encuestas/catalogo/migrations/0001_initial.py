# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Catalogo'
        db.create_table(u'catalogo_catalogo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
        ))
        db.send_create_signal(u'catalogo', ['Catalogo'])

        # Adding model 'Carrera'
        db.create_table(u'catalogo_carrera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'catalogo', ['Carrera'])

        # Adding model 'Persona'
        db.create_table(u'catalogo_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('genero', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('edad', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'catalogo', ['Persona'])

        # Adding model 'Pregunta'
        db.create_table(u'catalogo_pregunta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(default='', max_length=512)),
            ('catalogo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Catalogo'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'catalogo', ['Pregunta'])

        # Adding model 'Respuesta'
        db.create_table(u'catalogo_respuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(default='', max_length=512)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Pregunta'])),
        ))
        db.send_create_signal(u'catalogo', ['Respuesta'])

        # Adding model 'Seleccion'
        db.create_table(u'catalogo_seleccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['catalogo.Persona'])),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['catalogo.Pregunta'])),
            ('respuesta', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['catalogo.Respuesta'])),
        ))
        db.send_create_signal(u'catalogo', ['Seleccion'])


    def backwards(self, orm):
        # Deleting model 'Catalogo'
        db.delete_table(u'catalogo_catalogo')

        # Deleting model 'Carrera'
        db.delete_table(u'catalogo_carrera')

        # Deleting model 'Persona'
        db.delete_table(u'catalogo_persona')

        # Deleting model 'Pregunta'
        db.delete_table(u'catalogo_pregunta')

        # Deleting model 'Respuesta'
        db.delete_table(u'catalogo_respuesta')

        # Deleting model 'Seleccion'
        db.delete_table(u'catalogo_seleccion')


    models = {
        u'catalogo.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'catalogo.catalogo': {
            'Meta': {'object_name': 'Catalogo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'})
        },
        u'catalogo.persona': {
            'Meta': {'object_name': 'Persona'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'genero': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogo.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'catalogo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Catalogo']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '512'})
        },
        u'catalogo.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Pregunta']"}),
            'texto': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '512'})
        },
        u'catalogo.seleccion': {
            'Meta': {'object_name': 'Seleccion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['catalogo.Persona']"}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['catalogo.Pregunta']"}),
            'respuesta': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['catalogo.Respuesta']"})
        }
    }

    complete_apps = ['catalogo']