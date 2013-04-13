# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'groups_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_eu', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_es', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('markitup.fields.MarkupField')(default='', max_length=500, no_rendered_field=True, blank=True)),
            ('description_eu', self.gf('markitup.fields.MarkupField')(default='', max_length=500, null=True, blank=True, no_rendered_field=True)),
            ('description_es', self.gf('markitup.fields.MarkupField')(default='', max_length=500, null=True, blank=True, no_rendered_field=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_description_eu_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_description_es_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'groups', ['Group'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'groups_group')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'groups.group': {
            'Meta': {'object_name': 'Group'},
            '_description_es_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_eu_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'no_rendered_field': 'True', 'blank': 'True'}),
            'description_es': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'description_eu': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_eu': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        }
    }

    complete_apps = ['groups']