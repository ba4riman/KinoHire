# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BlogPost.title'
        db.delete_column('cinema_blogpost', 'title')

        # Adding field 'BlogPost.id_post'
        db.add_column('cinema_blogpost', 'id_post',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['cinema.Movie']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'BlogPost.title'
        raise RuntimeError("Cannot reverse this migration. 'BlogPost.title' and its values cannot be restored.")
        # Deleting field 'BlogPost.id_post'
        db.delete_column('cinema_blogpost', 'id_post_id')


    models = {
        'cinema.actor': {
            'Meta': {'object_name': 'Actor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cinema.blogpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Movie']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
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