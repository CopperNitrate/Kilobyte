[app]

# (str) Title of your application
title = Kilobyte AI

# (str) Package name (no spaces or special characters)
package.name = kilobyte

# (str) Package domain (needed for Android package naming: org.kilobyte.kilobyte)
package.domain = org.kilobyte

# (str) Source code where the main.py or app.py lives
source.dir = .

# (list) Source files to include (crucial for loading your HTML/CSS/JS frontend)
source.include_exts = py,png,jpg,html,css,js,json,txt

# (list) Application requirements
# Keep C-dependencies out to prevent compilation crashes in p4a
requirements = python3,flask,flask-cors,requests,urllib3,certifi

# (str) Application version
version = 1.0

# (list) Permissions needed for local networking and web calls
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API (33 = Android 13)
android.api = 33

# (int) Minimum Android API supported (21 = Android 5.0)
android.minapi = 21

# (str) Android NDK version pinned for build stability
android.ndk = 25b

# (bool) Auto-accept SDK license agreements during build
android.accept_sdk_licenses = True

# (str) Supported CPU Architectures (arm64-v8a covers almost all modern Android phones)
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
