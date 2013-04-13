# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attachment'
        db.create_table(u'attachments_attachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_attachments.attachment_set', null=True, to=orm['contenttypes.ContentType'])),
            ('oembed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('creation', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='_slug', unique_with=())),
        ))
        db.send_create_signal(u'attachments', ['Attachment'])

        # Adding model 'ExternalAttachment'
        db.create_table(u'attachments_externalattachment', (
            (u'attachment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['attachments.Attachment'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'attachments', ['ExternalAttachment'])

        # Adding model 'InternalAttachment'
        db.create_table(u'attachments_internalattachment', (
            (u'attachment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['attachments.Attachment'], unique=True, primary_key=True)),
            ('file', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'attachments', ['InternalAttachment'])


    def backwards(self, orm):
        # Deleting model 'Attachment'
        db.delete_table(u'attachments_attachment')

        # Deleting model 'ExternalAttachment'
        db.delete_table(u'attachments_externalattachment')

        # Deleting model 'InternalAttachment'
        db.delete_table(u'attachments_internalattachment')


    models = {
        u'attachments.attachment': {
            'Meta': {'ordering': "('-creation',)", 'object_name': 'Attachment'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oembed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_attachments.attachment_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'_slug'", 'unique_with': '()'})
        },
        u'attachments.externalattachment': {
            'Meta': {'ordering': "('-creation',)", 'object_name': 'ExternalAttachment', '_ormbases': [u'attachments.Attachment']},
            u'attachment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['attachments.Attachment']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'attachments.internalattachment': {
            'Meta': {'ordering': "('-creation',)", 'object_name': 'InternalAttachment', '_ormbases': [u'attachments.Attachment']},
            u'attachment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['attachments.Attachment']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['attachments']