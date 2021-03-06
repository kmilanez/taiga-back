# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 11:34
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0013_historyentry_values_diff_cache'),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "history_historyentry"
                   ALTER COLUMN "delete_comment_user" TYPE jsonb USING to_json("delete_comment_user"::text)::jsonb,
                   ALTER COLUMN "comment_versions" TYPE jsonb USING to_json("comment_versions"::text)::jsonb,
                   ALTER COLUMN "values_diff_cache" TYPE jsonb USING to_json("values_diff_cache"::text)::jsonb,
                   ALTER COLUMN "user" TYPE jsonb USING to_json("user"::text)::jsonb,
                   ALTER COLUMN "diff" TYPE jsonb USING to_json("diff"::text)::jsonb,
                   ALTER COLUMN "snapshot" TYPE jsonb USING to_json("snapshot"::text)::jsonb,
                   ALTER COLUMN "values" TYPE jsonb USING to_json("values"::text)::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop
        ),
    ]
