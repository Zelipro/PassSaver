[app]
title = PassSaver
package.name = passaver
package.domain = org.example

version = 1.3
requirements = python3,kivy,kivymd,pillow

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db,svg
source.include_patterns = Pages/*,*.db,*.jpeg,*.jpg,*.png,*.svg

# Permissions Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
android.archs = arm64-v8a
orientation = portrait
