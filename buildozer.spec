[app]
title = PassSaver
package.name = passaver
package.domain = org.example

version = 1.4
requirements = python3,kivy,kivymd,pillow

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db,svg
source.include_patterns = Pages/*,*.db,*.jpeg,*.jpg,*.png,*.svg

# Configuration du clavier - VERSION SIMPLIFIÉE
android.add_src = .
android.windowSoftInputMode = adjustResize|stateHidden

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# Configuration pour permettre toutes les orientations
orientation = all
android.orientation = all
android.orientations = landscape,portrait,portrait-reverse,landscape-reverse
