# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Counter'
        db.create_table(u'projects_counter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('pause', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Task'])),
        ))
        db.send_create_signal(u'projects', ['Counter'])


    def backwards(self, orm):
        # Deleting model 'Counter'
        db.delete_table(u'projects_counter')


    models = {
        u'projects.counter': {
            'Meta': {'object_name': 'Counter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pause': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Task']"})
        },
        u'projects.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'start_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'projects.task': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'Task'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hours_worked': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']