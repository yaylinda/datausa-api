tell application "Terminal"
	do script ". ~/Virtualenvs/datausa-api/bin/activate; python  ~/Projects/datausa-api/scripts/fill_cache.py http://db.datausa.io geo"
	activate
end tell

tell application "Terminal"
	do script ". ~/Virtualenvs/datausa-api/bin/activate; python  ~/Projects/datausa-api/scripts/fill_cache.py http://db.datausa.io cip"
	activate
end tell

tell application "Terminal"
	do script ". ~/Virtualenvs/datausa-api/bin/activate; python  ~/Projects/datausa-api/scripts/fill_cache.py http://db.datausa.io soc"
	activate
end tell

tell application "Terminal"
	do script ". ~/Virtualenvs/datausa-api/bin/activate; python  ~/Projects/datausa-api/scripts/fill_cache.py http://db.datausa.io naics"
	activate
end tell
