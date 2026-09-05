[app]

# (str) Title of your application
title = Kilobyte AI

# (str) Package name (no spaces or special characters)
package.name = kilobyte

# (str) Package domain (needed for Android package naming: org.kilobyte.kilobyte)
package.domain = org.kilobyte

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,html,css,js,json,txt

# (list) Application requirements
requirements = python3,flask,flask-cors,requests,urllib3,certifi

# (str) Application version
version = 1.0

# (list) Permissions needed
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum Android API supported
android.minapi = 21

# (str) Pin build-tools version to avoid unaccepted v37 license prompt
android.build_tools_version = 33.0.2

# (str) Android NDK version pinned for stability
android.ndk = 25b

# (bool) Auto-accept SDK license agreements
android.accept_sdk_licenses = True

# (str) Supported CPU Architectures
android.archs = arm64-v8a

# (str) Screen orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (bool) Warn if buildozer is run as root
warn_on_root = 1
