[app]
title = Kilobyte AI
package.name = kilobyte
package.domain = org.kilobyte
source.dir = .
source.include_exts = py,png,jpg,html,css,js,json,txt

# Standard pure-python dependencies only
requirements = python3,flask,flask-cors,requests,urllib3,certifi

version = 1.0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_licenses = True
android.archs = arm64-v8a
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
