Plugin for CudaText.
Gives menu "Plugins / Open URL" with several commands to open URL (under first caret in editor) in browser. Commands:

- Chrome
- Chrome, private (incognito) mode
- Firefox
- Firefox, private mode
- Opera
- Opera, private mode
- IE
- IE, private mode

Plugin also handles double-click event in editor, and if URL is double-clicked, it shows menu to open this URL.

You can configure paths to browsers, using config file - to edit file, call menu "Options / Settings-plugins / Open URL".

Option "handle_click": boolean (0 or 1): enable action of clicking URL in text.
Option "action_on_click": number:
- If -1: click on URL shows menu of browsers to use
- If >=0: it's 0-based index of menu item in browsers menu, this choice is used instead of showing menu.


Author: Alexey Torgashin (CudaText)
License: MIT