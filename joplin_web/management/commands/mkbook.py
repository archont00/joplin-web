#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand
from logging import getLogger

# joplin_web
from joplin_web.joplin import Joplin

# create logger
logger = getLogger("joplin_web.jw")


class Command(BaseCommand):

    help = 'Add a notebook to Joplin'

    def add_arguments(self, parser):
        parser.add_argument('notebook', type=str, help="notebook name")

    def handle(self, *args, **options):
        """
            call the command to add a notebook
        """
        logger.info("launch joplin to make a notebook %s" % options['notebook'])

        joplin = Joplin()
        out, err, exitcode = joplin.mkbook(options['notebook'])
        return out.decode()