# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Movie.director'
        db.delete_column('cinema_movie', 'director_id')

        # Deleting field 'Movie.country'
        db.delete_column('cinema_movie', 'country_id')

        # Deleting field 'Movie.actor'
        db.delete_column('cinema_movie', 'actor_id')

        # Adding M2M table for field country on 'Movie'
        db.create_table('cinema_movie_country', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['cinema.movie'], null=False)),
            ('country', models.ForeignKey(orm['cinema.country'], null=False))
        ))
        db.create_unique('cinema_movie_country', ['movie_id', 'country_id'])

        # Adding M2M table for field director on 'Movie'
        db.create_table('cinema_movie_director', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['cinema.movie'], null=False)),
            ('director', models.ForeignKey(orm['cinema.director'], null=False))
        ))
        db.create_unique('cinema_movie_director', ['movie_id', 'director_id'])

        # Adding M2M table for field actor on 'Movie'
        db.create_table('cinema_movie_actor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['cinema.movie'], null=False)),
            ('actor', models.ForeignKey(orm['cinema.actor'], null=False))
        ))
        db.create_unique('cinema_movie_actor', ['movie_id', 'actor_id'])


    def backwards(self, orm):
        # Adding field 'Movie.director'
        db.add_column('cinema_movie', 'director',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['cinema.Director']),
                      keep_default=False)

        # Adding field 'Movie.country'
        db.add_column('cinema_movie', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['cinema.Country']),
                      keep_default=False)

        # Adding field 'Movie.actor'
        db.add_column('cinema_movie', 'actor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['cinema.Actor']),
                      keep_default=False)

        # Removing M2M table for field country on 'Movie'
        db.delete_table('cinema_movie_country')

        # Removing M2M table for field director on 'Movie'
        db.delete_table('cinema_movie_director')

        # Removing M2M table for field actor on 'Movie'
        db.delete_table('cinema_movie_actor')


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
            'actor': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cinema.Actor']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cinema.Country']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cinema.Director']", 'symmetrical': 'False'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cinema.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_release': ('django.db.models.fields.DateField', [], {'null': 'True'})
        }
    }

    complete_apps = ['cinema']