[app]
title = PassSaver
package.name = Zelipro_PassSaver
package.domain = org.example_PageSaver
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db,svg
source.include_patterns = Pages/*,*.db,*.jpeg,*.jpg,*.png,*.svg
version = 1.0
requirements = python3,kivy,kivymd,pillow
icon.filename = %(source.dir)s/Logo.svg

# Permissions Android
android.permissions = INTERNET,CALL_PHONE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.archs = arm64-v8a, armeabi-v7a
# Configuration pour permettre toutes les orientations
orientation = all
android.orientation = all
android.orientations = landscape,portrait,portrait-reverse,landscape-reve

android.add_src = .
android.gradle_dependencies = 
android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8
