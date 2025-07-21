[app]
title = PassSaver
package.name = passaver
package.domain = org.example

version = 1.2
requirements = python3,kivy,kivymd

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Permissions Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
android.archs = arm64-v8a
orientation = portrait
