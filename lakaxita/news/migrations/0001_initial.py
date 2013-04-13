# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title_eu', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title_es', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('text', self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True)),
            ('text_eu', self.gf('markitup.fields.MarkupField')(default='', null=True, blank=True, no_rendered_field=True)),
            ('text_es', self.gf('markitup.fields.MarkupField')(default='', null=True, blank=True, no_rendered_field=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('frontpage', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Group'], null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=())),
            ('_text_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_text_eu_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_text_es_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'news', ['News'])

        # Adding M2M table for field attachments on 'News'
        db.create_table(u'news_news_attachments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news', models.ForeignKey(orm[u'news.news'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(u'news_news_attachments', ['news_id', 'attachment_id'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')

        # Removing M2M table for field attachments on 'News'
        db.delete_table('news_news_attachments')


    models = {
        u'attachments.attachment': {
            'Meta': {'ordering': "('-creation',)", 'object_name': 'Attachment'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oembed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_attachments.attachment_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'_slug'", 'unique_with': '()'})
        },
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
        },
        u'news.news': {
            'Meta': {'ordering': "['-published']", 'object_name': 'News'},
            '_text_es_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_text_eu_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'attachments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['attachments.Attachment']", 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['groups.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'text': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True'}),
            'text_es': ('markitup.fields.MarkupField', [], {'default': "''", 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'text_eu': ('markitup.fields.MarkupField', [], {'default': "''", 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']