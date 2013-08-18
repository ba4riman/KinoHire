# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Movie.genre'
        db.delete_column('cinema_movie', 'genre_id')

        # Adding M2M table for field genre on 'Movie'
        db.create_table('cinema_movie_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['cinema.movie'], null=False)),
            ('genre', models.ForeignKey(orm['cinema.genre'], null=False))
        ))
        db.create_unique('cinema_movie_genre', ['movie_id', 'genre_id'])


    def backwards(self, orm):
        # Adding field 'Movie.genre'
        db.add_column('cinema_movie', 'genre',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['cinema.Genre']),
                      keep_default=False)

        # Removing M2M table for field genre on 'Movie'
        db.delete_table('cinema_movie_genre')


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
            'time': ('django.db.models.fields.DateTimeField', [], {}),
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
        'cinema.likes': {
            'Meta': {'object_name': 'Likes'},
            'dislike': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {})
        },
        'cinema.movie': {
            'Meta': {'object_name': 'Movie'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Actor']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cinema.Director']"}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cinema.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_release': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['cinema']