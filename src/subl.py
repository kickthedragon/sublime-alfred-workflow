import sys
import os
import json
import plistlib

with open('info.plist', 'rb') as fp:
	info = plistlib.load(fp);

alfred_results = []


projects = info['variables']['PROJECTS_PATH']
for dir in os.listdir(projects):
	if dir == '.DS_Store':
		continue
	if os.path.exists(projects + '/' + dir + '/' + dir + '.sublime-project'):
		result = {
			"title": dir,
			"arg": projects + '/' + dir + '/' + dir + '.sublime-project',
			"icon": {
				"path": "icon/iu.png"
			}
		}
		alfred_results.append(result);
		# wf.add_item(title=dir, arg=projects + '/' + dir + '/' + dir + '.sublime-project', valid=True, icon='icon/iu.png')
	else:
		result = {
			"title": dir,
			"arg": projects + '/' + dir,
			"icon": {
				"path": "icon/iu.png"
			}
		}
		alfred_results.append(result);
		# wf.add_item(title=dir, arg=projects + '/' + dir, valid=True, icon='icon/iu.png')
response = json.dumps({
		"items": alfred_results
	})

sys.stdout.write(response)