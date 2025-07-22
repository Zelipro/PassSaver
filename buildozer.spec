[app]
title = PassSaver
package.name = passaver
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db,svg
source.include_patterns = Pages/*,*.db,*.jpeg,*.jpg,*.png,*.svg
version = 1.5
requirements = python3,kivy,kivymd,sqlite3,pillow
icon.filename = %(source.dir)s/Font.png

# Configuration du clavier - VERSION SIMPLIFIÉE
android.add_src = .
android.windowSoftInputMode = adjustResize

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.archs = arm64-v8a , armeabi-v7a  # Start with one arch to simplify
orientation = all
android.orientation = all
