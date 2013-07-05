#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Takes 5 command line arguments: a name, phone number, an email address, a project description, and an ip address.
# Saves the data request to a SQLite file.
# Returns a ticket ID.

import sys
import sqlite3
import datetime


def main():
    args = sys.argv[1:]
    log(args)
    
    if len(args) == 5:
        conn = sqlite3.connect('scraperwiki.sqlite')
        cursor = conn.cursor()
        command = """CREATE TABLE IF NOT EXISTS "request" (
                       "id" INTEGER PRIMARY KEY, "date", "name", "phone", "email", "ip", "description"
                     );"""
        cursor.execute(command)
        command = 'SELECT MAX("id") FROM "request";'
        cursor.execute(command)

        id = cursor.fetchone()[0] or 1999
        name = args[0].decode('utf-8')
        phone = args[1].decode('utf-8')
        email = args[2].decode('utf-8')
        description = args[3].decode('utf-8')
        ip = args[4].decode('utf-8')
        date = now()

        command = 'INSERT INTO "request" ("id", "date", "name", "phone", "email", "ip", "description") VALUES (?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(command, [ id + 1, date, name, phone, email, ip, description ])
        conn.commit()
        conn.close()

        print id + 1

    else:
        print 'Please supply 5 arguments: a name, a phone number, an email address, a project description and an IP address'
        sys.exit()


def log(thing):
    if(type(thing) == list):
        thing = "[%s]" % ', '.join(map(str, thing))
    with open('log.txt', 'a') as f:
        f.write("%s %s\n" % (now(), thing))


def now():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


if __name__ == "__main__":
    main()