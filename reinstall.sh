#!/bin/bash
rm -rf env
cd sportfriend/migrations
rm -rf 00*.py
cd ..
cd ..
rm -rf db.sqlite3
bash install.sh