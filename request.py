#!/usr/bin/env python 

# Takes 5 command line arguments: a name, phone number, an email address, a project description, and an ip address.
# Saves the data request to a SQLite file.
# Returns a ticket ID.

import sys
import sqlite3


def main():
    args = sys.argv[1:]
    
    if len(args) == 5:
        conn = sqlite3.connect('scraperwiki.sqlite')
        cursor = conn.cursor()
        command = """CREATE TABLE IF NOT EXISTS "request" (
                       "id" INTEGER PRIMARY KEY, "name", "phone", "email", "ip", "description"
                       "created" DATE DEFAULT (datetime('now', 'localtime'))
                     );"""
        cursor.execute(command)
        command = 'SELECT MAX("id") FROM "request";'
        cursor.execute(command)

        id = cursor.fetchone()[0] or 1999

        command = 'INSERT INTO "request" ("id", "name", "phone", "email", "ip", "description") VALUES (?, ?, ?, ?, ?, ?)'
        cursor.execute(command, [ id + 1, args[0], args[1], args[2], args[4], args[3] ])
        conn.commit()
        conn.close()
        
        print id + 1

    else:
        print 'Please supply 4 arguments: a name, a phone number, an email address and a project description'
        sys.exit()

if __name__ == "__main__":
    main()