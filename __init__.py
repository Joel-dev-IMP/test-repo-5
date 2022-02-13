# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <Hello World Addon>
#    Copyright (C) <2022>  <Joel Benkwitz>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "Hello World",
    "author": "Joel Benkwitz (BD)",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "warning": "",
    "tracker_url": "https://github.com/Joel-dev-IMP/jufo-demo-1/issues/new",
    "endpoint_url": "https://raw.githubusercontent.com/Joel-dev-IMP/test-repo-5/main/SuperAddonManager-EndpointN.json",
    "category": "General"
}


def register():
    print("Hello World!")


def unregister():
    pass
