# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'gallery_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_eu', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_es', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('markitup.fields.MarkupField')(default='', max_length=500, no_rendered_field=True, blank=True)),
            ('description_eu', self.gf('markitup.fields.MarkupField')(default='', max_length=500, null=True, blank=True, no_rendered_field=True)),
            ('description_es', self.gf('markitup.fields.MarkupField')(default='', max_length=500, null=True, blank=True, no_rendered_field=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['gallery.Category'])),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('_description_eu_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_description_es_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'gallery', ['Category'])

        # Adding M2M table for field attachments on 'Category'
        db.create_table(u'gallery_category_attachments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'gallery.category'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(u'gallery_category_attachments', ['category_id', 'attachment_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'gallery_category')

        # Removing M2M table for field attachments on 'Category'
        db.delete_table('gallery_category_attachments')


    models = {
        u'attachments.attachment': {
            'Meta': {'ordering': "('-creation',)", 'object_name': 'Attachment'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oembed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_attachments.attachment_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'_slug'", 'unique_with': '()'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gallery.category': {
            'Meta': {'object_name': 'Category'},
            '_description_es_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_eu_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'attachments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'no_rendered_field': 'True', 'blank': 'True'}),
            'description_es': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'description_eu': ('markitup.fields.MarkupField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_es': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_eu': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['gallery.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['gallery']