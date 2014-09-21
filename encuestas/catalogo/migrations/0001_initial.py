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
        ))
        db.send_create_signal(u'catalogo', ['Catalogo'])

        # Adding model 'Persona'
        db.create_table(u'catalogo_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Persona'])

        # Adding model 'Pregunta'
        db.create_table(u'catalogo_pregunta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('catalogo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Catalogo'])),
        ))
        db.send_create_signal(u'catalogo', ['Pregunta'])

        # Adding M2M table for field persona on 'Pregunta'
        m2m_table_name = db.shorten_name(u'catalogo_pregunta_persona')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta', models.ForeignKey(orm[u'catalogo.pregunta'], null=False)),
            ('persona', models.ForeignKey(orm[u'catalogo.persona'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_id', 'persona_id'])

        # Adding model 'Respuesta'
        db.create_table(u'catalogo_respuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Pregunta'])),
        ))
        db.send_create_signal(u'catalogo', ['Respuesta'])


    def backwards(self, orm):
        # Deleting model 'Catalogo'
        db.delete_table(u'catalogo_catalogo')

        # Deleting model 'Persona'
        db.delete_table(u'catalogo_persona')

        # Deleting model 'Pregunta'
        db.delete_table(u'catalogo_pregunta')

        # Removing M2M table for field persona on 'Pregunta'
        db.delete_table(db.shorten_name(u'catalogo_pregunta_persona'))

        # Deleting model 'Respuesta'
        db.delete_table(u'catalogo_respuesta')


    models = {
        u'catalogo.catalogo': {
            'Meta': {'object_name': 'Catalogo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogo.persona': {
            'Meta': {'object_name': 'Persona'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'catalogo.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'catalogo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Catalogo']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalogo.Persona']", 'symmetrical': 'False'})
        },
        u'catalogo.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Pregunta']"})
        }
    }

    complete_apps = ['catalogo']