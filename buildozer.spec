[app]
title = Kilobyte AI
package.name = kilobyte
package.domain = org.kilobyte
source.dir = .
source.include_exts = py,png,jpg,html,css,js
version = 1.0

requirements = python3,flask,flask-cors,g4f,requests,urllib3,certifi

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a