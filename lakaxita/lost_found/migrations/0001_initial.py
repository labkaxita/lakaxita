# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'lost_found_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_eu', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_es', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True, blank=True)),
            ('description_eu', self.gf('markitup.fields.MarkupField')(default='', null=True, blank=True, no_rendered_field=True)),
            ('description_es', self.gf('markitup.fields.MarkupField')(default='', null=True, blank=True, no_rendered_field=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('lost', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('found', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_description_eu_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_description_es_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'lost_found', ['Item'])

        # Adding model 'Notification'
        db.create_table(u'lost_found_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('reply_to', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lost_found.Item'])),
        ))
        db.send_create_signal(u'lost_found', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'lost_found_item')

        # Deleting model 'Notification'
        db.delete_table(u'lost_found_notification')


    models = {
        u'lost_found.item': {
            'Meta': {'ordering': "['-lost']", 'object_name': 'Item'},
            '_description_es_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_eu_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True', 'blank': 'True'}),
            'description_es': ('markitup.fields.MarkupField', [], {'default': "''", 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'description_eu': ('markitup.fields.MarkupField', [], {'default': "''", 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'found': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'lost': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_eu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'lost_found.notification': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Notification'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lost_found.Item']"}),
            'reply_to': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lost_found']