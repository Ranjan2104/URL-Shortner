# Developed by Amresh Ranjan.

import pyshorteners as ps

link = 'https://www.google.com'

setup = ps.Shortener()
x = (setup.tinyurl.short(link))

print(x)

