[app]
title = PassSaver
package.name = passaver
package.domain = org.example

version = 1.1
requirements = python3,kivy,kivymd

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
android.archs = arm64-v8a
orientation = portrait
