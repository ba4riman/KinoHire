# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.username'
        db.add_column('cinema_blogpost', 'username',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.username'
        db.delete_column('cinema_blogpost', 'username')


    models = {
        'cinema.actor': {
            'Meta': {'object_name': 'Actor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cinema.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_post': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cinema.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cinema.director': {
            'Meta': {'object_name': 'Director'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cinema.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cinema.movie': {
            'Meta': {'object_name': 'Movie'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Actor']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Director']"}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Genre']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_release': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['cinema']